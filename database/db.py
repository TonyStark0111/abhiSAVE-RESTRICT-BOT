import motor.motor_asyncio
import datetime
import config
from logger import LOGGER

logger = LOGGER(__name__)

class Database:
   
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id, name):
        return dict(
            id=id,
            name=name,
            session=None,
            daily_usage=0,
            limit_reset_time=None,
            private_daily_usage=0,
            private_limit_reset_time=None,
            last_public_request_time=None,
            last_private_request_time=None,
        )
   
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)
        logger.info(f"New user added: {id} - {name}")
   
    async def is_user_exist(self, id):
        return bool(await self.col.find_one({'id': int(id)}))
   
    async def total_users_count(self):
        return await self.col.count_documents({})

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_session(self, id, session):
        await self.col.update_one({'id': int(id)}, {'$set': {'session': session}})

    async def get_session(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('session')

    async def set_caption(self, id, caption):
        await self.col.update_one({'id': int(id)}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('caption')

    async def del_caption(self, id):
        await self.col.update_one({'id': int(id)}, {'$unset': {'caption': ""}})

    async def set_thumbnail(self, id, thumbnail):
        await self.col.update_one({'id': int(id)}, {'$set': {'thumbnail': thumbnail}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('thumbnail')

    async def del_thumbnail(self, id):
        await self.col.update_one({'id': int(id)}, {'$unset': {'thumbnail': ""}})

    async def add_premium(self, id, expiry_date):
        await self.col.update_one({'id': int(id)}, {
            '$set': {
                'is_premium': True,
                'premium_expiry': expiry_date,
                'daily_usage': 0,
                'limit_reset_time': None,
                'private_daily_usage': 0,
                'private_limit_reset_time': None
            }
        })

    async def remove_premium(self, id):
        await self.col.update_one({'id': int(id)}, {'$set': {'is_premium': False, 'premium_expiry': None}})

    async def check_premium(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('premium_expiry') if user and user.get('is_premium') else None

    async def get_premium_users(self):
        return self.col.find({'is_premium': True})

    async def ban_user(self, id):
        await self.col.update_one({'id': int(id)}, {'$set': {'is_banned': True}})

    async def unban_user(self, id):
        await self.col.update_one({'id': int(id)}, {'$set': {'is_banned': False}})

    async def is_banned(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('is_banned', False)

    async def set_dump_chat(self, id, chat_id):
        await self.col.update_one({'id': int(id)}, {'$set': {'dump_chat': int(chat_id)}})

    async def get_dump_chat(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('dump_chat')

    async def set_delete_words(self, id, words):
        await self.col.update_one({'id': int(id)}, {'$addToSet': {'delete_words': {'$each': words}}})

    async def get_delete_words(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('delete_words', [])

    async def remove_delete_words(self, id, words):
        await self.col.update_one({'id': int(id)}, {'$pull': {'delete_words': {'$in': words}}})

    async def set_replace_words(self, id, repl_dict):
        user = await self.col.find_one({'id': int(id)})
        current = user.get('replace_words', {})
        current.update(repl_dict)
        await self.col.update_one({'id': int(id)}, {'$set': {'replace_words': current}})

    async def get_replace_words(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('replace_words', {})

    async def remove_replace_words(self, id, words):
        user = await self.col.find_one({'id': int(id)})
        current = user.get('replace_words', {})
        for w in words:
            current.pop(w, None)
        await self.col.update_one({'id': int(id)}, {'$set': {'replace_words': current}})

    # ----- Public limits -----
    async def check_limit(self, id):
        user = await self.col.find_one({'id': int(id)})
        if not user or user.get('is_premium'):
            return False
        now = datetime.datetime.now()
        reset = user.get('limit_reset_time')
        if reset is None or now >= reset:
            await self.col.update_one({'id': int(id)}, {'$set': {'daily_usage': 0, 'limit_reset_time': None}})
            return False
        return user.get('daily_usage', 0) >= config.PUBLIC_DAILY_LIMIT

    async def add_traffic(self, id):
        user = await self.col.find_one({'id': int(id)})
        if user.get('is_premium'):
            return
        now = datetime.datetime.now()
        reset = user.get('limit_reset_time')
        if reset is None:
            new_reset = now + datetime.timedelta(hours=24)
            await self.col.update_one({'id': int(id)}, {'$set': {'daily_usage': 1, 'limit_reset_time': new_reset}})
        else:
            await self.col.update_one({'id': int(id)}, {'$inc': {'daily_usage': 1}})

    # ----- Private limits -----
    async def check_private_limit(self, id):
        user = await self.col.find_one({'id': int(id)})
        if not user or user.get('is_premium'):
            return False
        now = datetime.datetime.now()
        reset = user.get('private_limit_reset_time')
        if reset is None or now >= reset:
            await self.col.update_one({'id': int(id)}, {'$set': {'private_daily_usage': 0, 'private_limit_reset_time': None}})
            return False
        return user.get('private_daily_usage', 0) >= config.PRIVATE_DAILY_LIMIT

    async def add_private_traffic(self, id):
        user = await self.col.find_one({'id': int(id)})
        if user.get('is_premium'):
            return
        now = datetime.datetime.now()
        reset = user.get('private_limit_reset_time')
        if reset is None:
            new_reset = now + datetime.timedelta(hours=24)
            await self.col.update_one({'id': int(id)}, {'$set': {'private_daily_usage': 1, 'private_limit_reset_time': new_reset}})
        else:
            await self.col.update_one({'id': int(id)}, {'$inc': {'private_daily_usage': 1}})

    # ----- Cooldowns -----
    async def check_public_cooldown(self, id):
        user = await self.col.find_one({'id': int(id)})
        if not user or user.get('is_premium'):
            return 0
        last = user.get('last_public_request_time')
        if not last:
            return 0
        elapsed = (datetime.datetime.now() - last).total_seconds()
        remaining = config.PUBLIC_COOLDOWN - elapsed
        return int(remaining) if remaining > 0 else 0

    async def update_public_request_time(self, id):
        await self.col.update_one({'id': int(id)}, {'$set': {'last_public_request_time': datetime.datetime.now()}})

    async def check_private_cooldown(self, id):
        user = await self.col.find_one({'id': int(id)})
        if not user or user.get('is_premium'):
            return 0
        last = user.get('last_private_request_time')
        if not last:
            return 0
        elapsed = (datetime.datetime.now() - last).total_seconds()
        remaining = config.PRIVATE_COOLDOWN - elapsed
        return int(remaining) if remaining > 0 else 0

    async def update_private_request_time(self, id):
        await self.col.update_one({'id': int(id)}, {'$set': {'last_private_request_time': datetime.datetime.now()}})


db = Database(config.DB_URI, config.DB_NAME)

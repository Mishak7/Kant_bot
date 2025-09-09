import aiosqlite
from config.logger import logger

async def check_user_exists(telegram_id: int) -> bool:
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("SELECT id FROM Users WHERE telegram_id = ?", (telegram_id,))
            result = await cursor.fetchone()
            return result is not None
    except Exception as e:
        logger.error(f"Error checking user existence: {e}")
        return False


async def create_user(telegram_id: int, username: str):
    try:
        async with aiosqlite.connect('BFU.db') as db:
            await db.execute("""
                INSERT INTO Users (telegram_id, username, score, hearts, created_at, updated_at)
                VALUES (?, ?, 0, 5, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """, (telegram_id, username))
            await db.commit()
            return True
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return False

async def get_user_name(telegram_id: int) -> str:
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute(
                "SELECT username, score, hearts FROM Users WHERE telegram_id = ?",
                (telegram_id,)
            )
            result = await cursor.fetchone()
            return result if result else None
    except Exception as e:
        logger.error(f"Error getting user name: {e}")
        return None
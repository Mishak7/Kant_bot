import aiosqlite
from config.logger import logger

async def select_leaders_from_leaderboard():
    try:
        async with aiosqlite.connect('BFU.db') as db:
            cursor = await db.execute("""SELECT username, score FROM Users
                                        ORDER BY score DESC
                                        LIMIT 5""")
            best_users = await cursor.fetchall()

            medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
            lines_output = []

            for i, (user, score) in enumerate(best_users):
                medal = medals[i]
                lines_output.append(f'{medal} {user} - {score} баллов')

            final_leaderboard = '🏆Рейтинг лучших игроков:\n\n' + '\n'.join(lines_output)
            return final_leaderboard


    except Exception as e:
        logger.error(f"Error with showing leaderboard: {e}")
        return False




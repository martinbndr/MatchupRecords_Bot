from main import db, cursor
# scores(guild_id BIGINT, user_id BIGINT, opponent_id BIGINT, wins BIGINT DEFAULT 0, losses BIGINT DEFAULT 0)
class ScoreKeeper:
    def __init__(self) -> None:
        pass

    def checkMatchupRecord(self, user1: int, user2: int, guildid: int):
        cursor.execute('SELECT * FROM scores WHERE user_id = ? AND guild_id = ?', (user1, guildid))
        userdata1 = cursor.fetchone()
        if not userdata1:
            cursor.execute('INSERT INTO scores VALUES (?,?,?)')
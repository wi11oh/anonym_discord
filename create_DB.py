import sqlite3
# anonym_discord.pyと同じディレクトリで初回だけ実行

dbname = 'anonym_discord_log.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute("""

    CREATE TABLE logs(
        message_id INTEGER PRIMARY KEY,
        author STRING,
        content STRING,
        time TIMESTAMP,
        moderator STRING
    )

""")


conn.commit()
conn.close()

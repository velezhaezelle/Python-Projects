import sqlite3


# =====================================================
# CREATE DATABASE
# =====================================================

def init_db():

    conn = sqlite3.connect("database/lms.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        xp INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


# =====================================================
# REGISTER USER
# =====================================================

def register_user(username, password):

    conn = sqlite3.connect("database/lms.db")
    cur = conn.cursor()

    try:

        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


# =====================================================
# LOGIN USER
# =====================================================

def login_user(username, password):

    conn = sqlite3.connect("database/lms.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()

    conn.close()

    return user


# =====================================================
# ADD XP
# =====================================================

def add_xp(username, amount):

    conn = sqlite3.connect("database/lms.db")
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET xp = xp + ? WHERE username = ?",
        (amount, username)
    )

    conn.commit()
    conn.close()


# =====================================================
# GET XP
# =====================================================

def get_xp(username):

    conn = sqlite3.connect("database/lms.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT xp FROM users WHERE username = ?",
        (username,)
    )

    xp = cur.fetchone()

    conn.close()

    if xp:
        return xp[0]

    return 0


# =====================================================
# RUN DATABASE
# =====================================================

if __name__ == "__main__":

    init_db()

    print("Database initialized.")
import sqlite3 
import telebot 

db = sqlite3.connect('data/database.db')
cursor = db.cursor()

bot = telebot.TeleBot("token")


db.execute('CREATE TABLE IF NOT EXISTS gr(CID INT UNIQUE)')
db.execute('CREATE TABLE IF NOT EXISTS users(CID INT UNIQUE)')

def add_user(cid):
    try:
        db.execute("""INSERT INTO users(CID)
            VALUES(?)""",(cid))
    except:
        pass
def add_gr(cid):
    try:
        db.execute("""INSERT INTO gr(CID)
            VALUES(?)""",(cid))
    except:
        pass

def ads_send(message):
    try:
        text = message.text
        if text=="🚫 Bekor qilish":
            bot.send_photo(message.chat.id,photo="https://t.me/the_solodest/178",caption="🚫 Xabar yuborish bekor qilindi !")
        else:
            cursor.execute("SELECT cid FROM users")
            rows = cursor.fetchall()
            for i in rows:
                chat_id = i[0]
                print(chat_id)
                bot.send_message(chat_id,message.text)
            bot.send_photo(admin_id,photo="https://t.me/the_solodest/178",caption="<b>✅ Xabar hamma foydalanuvchiga yuborildi!</b>")
    except:
        pass
def get_stat():
    cursor.execute("SELECT COUNT(CID) FROM users")
    rows = cursor.fetchall()
    return rows[0][0]
def for_send(message):
    text = message.text
    if text == "🚫 Bekor qilish":
        bot.send_photo(message.chat.id,photo="https://t.me/the_solodest/178",caption="🚫 Xabar yuborish bekor qilindi!")
    else:
        cursor.execute("SELECT cid FROM users")
        rows = cursor.fetchall()
        for row in rows:
            try:
                chat_id = row[0]
                print(chat_id)
                bot.forward_message(chat_id, admin_id, message.message_id)
            except Exception as e:
                print(e)
        bot.send_message(admin_id, "✅ Xabar hamma foydalanuvchiga yuborildi!")
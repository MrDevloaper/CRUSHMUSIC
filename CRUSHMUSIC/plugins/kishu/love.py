from pyrogram import Client, filters
import random
from  CRUSHMUSIC import app

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "The flame is there, it just needs a little fuel."
            "A promising start, with so much more to come."
            "The first step toward something truly special."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "The bond is growing. Keep feeding it with care."
            "There's real potential. Stay committed and watch it flourish."
            "Love is taking root. Keep watering it with effort and patience."
        ])
    else:
        return random.choice([
            "A love story written in the stars!"
            "Soulmates found—treasure this connection."
            "Meant to be! Wishing you endless happiness."
        ])
        
@app.on_message(filters.command("love", prefixes="/"))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"{name1}💕 + {name2}💕 = {love_percentage}%\n\n{love_message}"
    else:
        response = "Please enter two names after /love command."
    app.send_message(message.chat.id, response)

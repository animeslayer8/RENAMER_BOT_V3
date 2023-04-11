import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','6072652725:AAHUqLyazJlWpmMXCxyz1lD-EKNFHw43EFo')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Total User:- {total_user()}\nBot :- @Rename_kuski_2_bot\nCreater :- @Katsuki_warlord\nLanguage :-Python3\nLibrary :- Pyrogram 2.0\nServer :- Heroku\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} ",quote=True)

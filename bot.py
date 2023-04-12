import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6264709188:AAH06CYhmnIC6vDBsvzs7aPJsQcWURUstr0")

API_ID = int(os.environ.get("API_ID", "7165358"))

API_HASH = os.environ.get("API_HASH", "304228f1dc7b9c86ef1c8d83cdc5da85")

STRING = os.environ.get("STRING", "BQBtVa4ASKZEjK1fJTlgpFth35pgaRIp_0NhCDM7W7vq7ajkn-K5q1NjVHjA9owehPd1w04f5Kut8F9ZfTTqDpHSnzObARoNwlWEyFP1EuE_BvN5H7MZkpSTJxSEbAMmwJa9Z2OkE42z4a0ehcpZsnhDlOPmgrO8l7gzus8nWkKwX1g719fLFXm1lpfnHsrZRM8IRGsnvMNqewumoxLzDfQmANwPJFEWFhemfSjXKyA7rIyqr1y-YhDiAw7U1xBIbd2yC-WgGAoAxbj7nckXN3ZLxuzoWy5nsffhOg3t8i2JFdACNlvNp9gSLd_U11X7wR8FOtmnqkxqKu6a7F6XmVaOCh5uQAAAAAFmd66DAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()

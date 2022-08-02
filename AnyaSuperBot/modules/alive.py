#Owned By @TheKaizuryu & @Xelcius

from telethon import events, Button, custom
import re, os
from AnyaSuperBot.events import register
from AnyaSuperBot import telethn as tbot
from AnyaSuperBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/aec92f8fb1049a82a8fc9.jpg"
@register(pattern=("/alive"))
async def awake(event):
  Saber = f"**パワー Hii {event.sender.first_name} I'm General Esdeath** \n\n"
  Saber += "**パワー I'm Property OF @AztecSupport**\n\n"
  Saber += "**パワー Esdeath 剣: Version **\n\n"
  Saber += "**パワー Creator:** [U N K N O W N](t.me/XTheAnonymous)\n\n"
  Saber += "**パワー python-Telegram-Bot: 13.11**\n\n"
  BUTTON = [[Button.url("Support", "https://t.me/AztecSupport"), Button.url("Updates", "https://t.me/AogiriNetwork")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=Saber,  buttons=BUTTON)

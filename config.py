# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#
import random
import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8154426339")
APP_ID = int(os.environ.get("APP_ID", "26254064")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002170811388")) #Your db channel Id
OWNER = os.environ.get("OWNER", "OnlyNoco") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "5296584067")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://abidabdullahcloud:abidabdullah1425@cluster0.3ebwbfh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "AnimeCrisp")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "0"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/OnlyNoco")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PICS = os.environ.get("START_PIC", "https://envs.sh/bjb.mp4 https://envs.sh/bjP.mp4 https://envs.sh/bjw.mp4 https://envs.sh/bj0.mp4 https://envs.sh/bjS.mp4 https://envs.sh/bjW.mp4 https://envs.sh/bjB.mp4 https://envs.sh/bjI.mp4 https://envs.sh/bjn.mp4 https://envs.sh/bjT.mp4 https://envs.sh/bjZ.mp4 https://envs.sh/bjL.mp4 https://envs.sh/bj5.mp4 https://envs.sh/bjY.mp4 https://envs.sh/bjC.mp4").split(" ")

def get_random_pic():
    return random.choice(START_PICS)
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>HELP SECTION\n\n/report <write message> - send report to owner</blockquote></b>"
ABOUT_TXT = (
    "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ sᴘᴀᴄᴇ</b>\n"
    "──────────────────────\n"
    "<b>ᴏᴡɴᴇʀ:</b> <a href='https://t.me/OnlyNoco'>OnlyNoco</a>\n"
    "<b>ᴡᴇʙsɪᴛᴇ:</b> <a href='https://onlynoco.vercel.app'>Website</a>\n\n"
    "<b>ᴄʜᴀɴɴᴇʟs</b>\n"
    "──────────────────────\n"
    "• <a href='https://t.me/HeavenlySubs'>ʙᴛᴛʜ</a>\n"
    "• <a href='https://t.me/+O7PeEMZOAoMzYzVl'>ʜᴇɴᴛᴀɪ</a>\n"
    "• <a href='https://t.me/OngoingAnimeCrisp'>ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ</a>\n"
    "• <a href='https://t.me/CrispAnime'>ғɪɴɪsʜᴇᴅ ᴀɴɪᴍᴇ</a>\n"
    "• <a href='https://t.me/AnimeCrispNews'>ᴀɴɪᴍᴇ ɴᴇᴡs</a>\n"
    "──────────────────────\n"
    "<i>ᴀʟʟ ɪɴ ᴏɴᴇ ᴘʟᴀᴄᴇ.</i>"
)
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\n<blockquote> ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b><blockquote>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b></blockquote>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
<b>›› /delreq :</b> Rᴇᴍᴏᴠᴇᴅ ʟᴇғᴛᴏᴠᴇʀ ɴᴏɴ-ʀᴇǫᴜᴇsᴛ ᴜsᴇʀs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @nova_flix</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"
#--------------------------------------------


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

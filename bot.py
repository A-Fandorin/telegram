{\rtf1\ansi\ansicpg1251\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import os\
import telebot\
from apscheduler.schedulers.background import BackgroundScheduler\
from apscheduler.triggers.daily import DailyTrigger\
import datetime\
\
# \uc0\u1055 \u1086 \u1083 \u1091 \u1095 \u1080 \u1090 \u1077  \u1090 \u1086 \u1082 \u1077 \u1085  \u1074 \u1072 \u1096 \u1077 \u1075 \u1086  \u1073 \u1086 \u1090 \u1072  \u1080 \u1079  \u1087 \u1077 \u1088 \u1077 \u1084 \u1077 \u1085 \u1085 \u1099 \u1093  \u1086 \u1082 \u1088 \u1091 \u1078 \u1077 \u1085 \u1080 \u1103 \
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")\
bot = telebot.TeleBot(bot_token)\
\
# \uc0\u1057 \u1086 \u1079 \u1076 \u1072 \u1081 \u1090 \u1077  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1102  \u1076 \u1083 \u1103  \u1086 \u1090 \u1087 \u1088 \u1072 \u1074 \u1082 \u1080  \u1077 \u1078 \u1077 \u1076 \u1085 \u1077 \u1074 \u1085 \u1099 \u1093  \u1085 \u1072 \u1087 \u1086 \u1084 \u1080 \u1085 \u1072 \u1085 \u1080 \u1081 \
def daily_reminder():\
    current_time = datetime.datetime.now().strftime("%H:%M:%S")\
    chat_id = "YOUR_CHAT_ID"  # \uc0\u1047 \u1072 \u1084 \u1077 \u1085 \u1080 \u1090 \u1077  \u1085 \u1072  \u1074 \u1072 \u1096  ID \u1095 \u1072 \u1090 \u1072  \u1080 \u1083 \u1080  \u1087 \u1086 \u1083 \u1100 \u1079 \u1086 \u1074 \u1072 \u1090 \u1077 \u1083 \u1103 \
    bot.send_message(chat_id, f"Daily reminder sent at \{current_time\}")\
\
# \uc0\u1057 \u1086 \u1079 \u1076 \u1072 \u1081 \u1090 \u1077  \u1086 \u1073 \u1098 \u1077 \u1082 \u1090  \u1087 \u1083 \u1072 \u1085 \u1080 \u1088 \u1086 \u1074 \u1097 \u1080 \u1082 \u1072  \u1079 \u1072 \u1076 \u1072 \u1095 \
scheduler = BackgroundScheduler()\
trigger = DailyTrigger(hour=10, minute=0, second=0)  # \uc0\u1053 \u1072 \u1087 \u1088 \u1080 \u1084 \u1077 \u1088 , \u1082 \u1072 \u1078 \u1076 \u1099 \u1081  \u1076 \u1077 \u1085 \u1100  \u1074  10:00 AM\
\
# \uc0\u1044 \u1086 \u1073 \u1072 \u1074 \u1100 \u1090 \u1077  \u1079 \u1072 \u1076 \u1072 \u1095 \u1091  \u1074  \u1087 \u1083 \u1072 \u1085 \u1080 \u1088 \u1086 \u1074 \u1097 \u1080 \u1082 \
scheduler.add_job(daily_reminder, trigger=trigger)\
\
# \uc0\u1047 \u1072 \u1087 \u1091 \u1089 \u1090 \u1080 \u1090 \u1077  \u1087 \u1083 \u1072 \u1085 \u1080 \u1088 \u1086 \u1074 \u1097 \u1080 \u1082 \
scheduler.start()\
\
# \uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1082 \u1072  \u1082 \u1086 \u1084 \u1072 \u1085 \u1076 \u1099  /start\
@bot.message_handler(commands=['start'])\
def start(message):\
    bot.send_message(message.chat.id, "\uc0\u1055 \u1088 \u1080 \u1074 \u1077 \u1090 ! \u1071  \u1090 \u1074 \u1086 \u1081  \u1073 \u1086 \u1090  \u1076 \u1083 \u1103  \u1085 \u1072 \u1087 \u1086 \u1084 \u1080 \u1085 \u1072 \u1085 \u1080 \u1081 . "\
                                      "\uc0\u1044 \u1086 \u1073 \u1072 \u1074 \u1100  \u1079 \u1072 \u1076 \u1072 \u1095 \u1080 , \u1080  \u1103  \u1073 \u1091 \u1076 \u1091  \u1085 \u1072 \u1087 \u1086 \u1084 \u1080 \u1085 \u1072 \u1090 \u1100  \u1090 \u1077 \u1073 \u1077  \u1086  \u1085 \u1080 \u1093 !")\
\
# \uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1082 \u1072  \u1082 \u1086 \u1084 \u1072 \u1085 \u1076 \u1099  /add\
@bot.message_handler(commands=['add'])\
def add_task(message):\
    # \uc0\u1047 \u1076 \u1077 \u1089 \u1100  \u1084 \u1086 \u1078 \u1085 \u1086  \u1076 \u1086 \u1073 \u1072 \u1074 \u1080 \u1090 \u1100  \u1083 \u1086 \u1075 \u1080 \u1082 \u1091  \u1076 \u1083 \u1103  \u1076 \u1086 \u1073 \u1072 \u1074 \u1083 \u1077 \u1085 \u1080 \u1103  \u1079 \u1072 \u1076 \u1072 \u1095 \u1080 \
    bot.send_message(message.chat.id, "\uc0\u1047 \u1072 \u1076 \u1072 \u1095 \u1072  \u1091 \u1089 \u1087 \u1077 \u1096 \u1085 \u1086  \u1076 \u1086 \u1073 \u1072 \u1074 \u1083 \u1077 \u1085 \u1072 !")\
\
# \uc0\u1047 \u1072 \u1087 \u1091 \u1089 \u1082  \u1073 \u1086 \u1090 \u1072 \
bot.polling()\
}
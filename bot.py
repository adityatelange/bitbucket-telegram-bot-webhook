import telepot

from config import TOKEN, OWNER_ID, NOTIFY_GRP_IDS


class Bot:
    def __init__(self, data):
        self.token = TOKEN
        self.owner = OWNER_ID

        self.bot = telepot.Bot(self.token)
        for x in NOTIFY_GRP_IDS:
            self.bot.sendMessage(chat_id=x, text=data, parse_mode='Markdown')

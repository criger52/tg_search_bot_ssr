TOKEN='7570207199:AAFpnnbqhotSV5WYzVV2qE3Zay8yGV8m410'
from aiogram.types import BotCommand
bot_commands = [
    BotCommand(command="/help", description="Get info about me"),
    BotCommand(command="/qna", description="set bot for a QnA task"),
    BotCommand(command="/chat", description="set bot for free chat")
    ]

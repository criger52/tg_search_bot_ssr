
from aiogram.types import BotCommand
bot_commands = [
    BotCommand(command="/help", description="Get info about me"),
    BotCommand(command="/qna", description="set bot for a QnA task"),
    BotCommand(command="/chat", description="set bot for free chat")
    ]

statuses = {
'status_text':0,
'status_word':0,
}
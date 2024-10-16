from gc import callbacks

from aiogram import F,Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup



router = Router()

class MyForm(StatesGroup):
    waiting_for_message = State()

status_text = 0
text = ''
search_word = ''

status_word = 0

@router.message(CommandStart())
async def cmd_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text='Найти слово в тексте',callback_data='1')
    await message.answer('Что будем делать❓❓❓',reply_markup=builder.as_markup())


@router.callback_query(F.data == '1')
async def sub_menu(callback: CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    builder.button(text="Отправить текст 📜", callback_data="text1")
    builder.button(text="Отправить искомое выражение 📝", callback_data="word")
    builder.button(text="Настройки ⚙️", callback_data="settings")
    builder.button(text="Назад 🔙", callback_data="back")
    builder.button(text="Искать 🔎", callback_data="back")
    builder.adjust(1)

    await callback.message.answer('Выберите что делать😁', reply_markup=builder.as_markup())

@router.callback_query(F.data == 'back')
async def cmd_back(callback: CallbackQuery):
    await callback.message.delete()
    await cmd_start(callback.message)

@router.message()
async def sub_menu(message: Message):
    builder = InlineKeyboardBuilder()
    if status_text == 0:
        builder.button(text="Отправить текст 📜", callback_data="text1")
    elif status_text == 1:
        builder.button(text="Изменить текст 📜", callback_data="text2")
    if status_word == 0:
        builder.button(text="Отправить искомое выражение 📝", callback_data="word1")
    elif status_word == 1:
        builder.button(text="Изменить искомое выражение 📝", callback_data="word2")
    builder.button(text="Настройки ⚙️", callback_data="settings")
    builder.button(text="Назад 🔙", callback_data="back")
    builder.button(text="Искать 🔎", callback_data="back")
    builder.adjust(1)

    await message.answer('Выберите что делать😁', reply_markup=builder.as_markup())


@router.callback_query(F.data == 'settings')
async def cmd_text(callback: CallbackQuery):
    await callback.message.answer(f'text:{text} word:{search_word}')

@router.callback_query(F.data == 'text1')
async def cmd_text(callback: CallbackQuery):
    global status_text
    status_text = 1

    await callback.message.edit_text(f'Напишите текст или отправьте файлом:')
    async def input_text(message: Message):
        await  message.answer(message.text)
        message.text = text

@router.message()
async def process_user_message(message: Message):
    await  message.answer('dsss')
    # await sub_menu(message)

#
# @router.callback_query(F.data == 'word')
# async def input_word(callback: CallbackQuery):
#     await callback.message.edit_text('send search word pls:')
#     global word
#     word = callback.message.text
#     status_word = 1
#     print(word)
#     while word == '':
#         await show_sub_menu_cmd(callback.message)

@router.callback_query(F.data == 'word')
async def cmd_word(callback: CallbackQuery  ,state:FSMContext):
    global status_word
    status_word = 1
    await callback.message.edit_text('Напишите искомое выражение или отправьте файлом:')
    await state.set_state(MyForm.waiting_for_message)
    await state.update_data(callback_message=callback.message)


@router.message(MyForm.waiting_for_message)
async def process_user_message(message: Message):
    global user_message
    user_message = message.text
    print(user_message)



@router.message(Command("dice"))
async def cmd_dice(message: Message):
    for i in range(5):
        await message.answer_dice(emoji="🎰")






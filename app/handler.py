from aiogram import F,Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup



import os
router = Router()

class Form(StatesGroup):
    waiting_text = State()
    waiting_word = State()

statuses = {
'status_text':0,
'status_word':0,
}


@router.message(CommandStart())
async def cmd_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text='Найти слово в тексте',callback_data='1')
    await message.answer('Что будем делать❓❓❓',reply_markup=builder.as_markup())


@router.callback_query(F.data == '1')
async def show_sub_menu_after_start_cmd(callback: CallbackQuery):
    await callback.message.delete()
    builder = InlineKeyboardBuilder()
    if statuses['status_text'] == 0:
        builder.button(text="Отправить текст 📜", callback_data="text")
    elif statuses['status_text'] == 1:
        builder.button(text="Изменить текст 📜", callback_data="text")
    if statuses['status_word'] == 0:
        builder.button(text="Отправить искомое выражение 📝", callback_data="word")
    elif statuses['status_word'] == 1:
        builder.button(text="Изменить искомое выражение 📝", callback_data="word")
    builder.button(text="Настройки ⚙️", callback_data="settings")
    builder.button(text="Назад 🔙", callback_data="back_start")
    builder.button(text="Искать 🔎", callback_data="back")
    builder.adjust(1)

    await callback.message.answer('Выберите что делать😁', reply_markup=builder.as_markup())

@router.message(F.data == 'Ahaha You cant get in here,nononono')
async def show_sub_menu_cmd(message: Message):
    builder = InlineKeyboardBuilder()
    if statuses['status_text'] == 0:
        builder.button(text="Отправить текст 📜", callback_data="text")
    elif statuses['status_text'] == 1:
        builder.button(text="Изменить текст 📜", callback_data="text")
    if statuses['status_word'] == 0:
        builder.button(text="Отправить искомое выражение 📝", callback_data="word")
    elif statuses['status_word'] == 1:
        builder.button(text="Изменить искомое выражение 📝", callback_data="word")
    builder.button(text="Настройки ⚙️", callback_data="settings")
    builder.button(text="Назад 🔙", callback_data="back_start")
    builder.button(text="Искать 🔎", callback_data="back")
    builder.adjust(1)

    await message.answer('Выберите что делать😁', reply_markup=builder.as_markup())


#изменение/запись text
@router.callback_query(F.data == 'text')
async def ask_input_text(callback: CallbackQuery,state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад 🔙", callback_data="back")
    await callback.message.edit_text('Отправьте текст или файл с ним:',reply_markup=builder.as_markup())
    await state.set_state(Form.waiting_text)
#ожидание отправки сообщения
@router.message_handler(Form.waiting_text)
async def input_text(message: Message,state: FSMContext):
    if message.text:
        user_text = message.text
        print(user_text)
        statuses['status_text'] = 1
        await show_sub_menu_cmd(message)
        await state.clear()
    elif message.document:
        doc = message.document
        doc_path = f'downloads/{doc.file_name}'
        try:
            await message.document.dow
            await message.reply(f"Файл {doc.file_name} успешно загружен!")
        except Exception as e:
            await message.reply(f"Ошибка при скачивании файла: {str(e)}")

#изменение/запись word
@router.callback_query(F.data == 'word')
async def ask_input_word(callback: CallbackQuery,state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад 🔙", callback_data="back")
    await callback.message.edit_text('send search word pls:',reply_markup=builder.as_markup())#надопопробовать убрать кнопку нахад после ввода текста???
    await state.set_state(Form.waiting_word)
#ожидание отправки сообщения
@router.message(Form.waiting_word)
async def input_word(message: Message,state: FSMContext):
    user_word = message.text
    print(user_word)
    statuses['status_word'] = 1
    await show_sub_menu_cmd(message)
    await state.clear()


#назад
@router.callback_query(F.data == 'back')
async def go_back(callback: CallbackQuery):
    await callback.message.delete()
    await show_sub_menu_cmd(callback.message)

#назад к старту
@router.callback_query(F.data == 'back')
async def go_back(callback: CallbackQuery):
    await callback.message.delete()
    await cmd_start(callback.message)


#настройки
@router.callback_query(F.data == 'settings')
async def show_settings(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()

    builder.button(text='Учет регистра✅',callback_data='register')
    builder.button(text='Замена❌', callback_data='replace')
    builder.button(text='Точный поиск❌',callback_data='inexact_search')
    builder.button(text="Назад 🔙", callback_data="back_start")
    builder.button(text='Поиск по нескольким файлам❌💀',callback_data='many_files')
    builder.adjust(2, 2)
    await callback.message.edit_text('Настройки',reply_markup=builder.as_markup())

#учет регистра
@router.callback_query(F.data == 'register')
async def off_on_register(callback: CallbackQuery):
    pass
#замена
@router.callback_query(F.data == 'register')
async def off_on_replace(callback: CallbackQuery):
    pass
#неточный поиск
@router.callback_query(F.data == 'inexact_search')
async def off_on_replace(callback: CallbackQuery):
    pass
#неточный поиск
@router.callback_query(F.data == 'many_files')
async def off_on_replace(callback: CallbackQuery):
    pass
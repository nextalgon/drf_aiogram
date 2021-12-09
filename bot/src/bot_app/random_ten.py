from aiogram import types
from aiogram.dispatcher import FSMContext
from app import bot, dp
from data_fetcher import get_random
from keyboards import markup
from states import GameStates


@dp.message_handler(commands='try_ten', state='*')
async def try_ten(msg: types.Message, state: FSMContext):
    await GameStates.random_ten.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('gender')
        data['words'] = res.get('words')
        await msg.reply(f'№: {data["step"]} из 10. Слово: {data["words"]}', reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data in ['мужской', 'женский', 'средный'], state=GameStates.random_ten)
async def button_click(call: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(call.id)
    answer = call.data
    async with state.proxy() as data:
        if answer == data.get('answer'):
            res = await get_random()
            data['step'] += 1
            data['answer'] = res.get('gender')
            data['words'] = res.get('words')
            if data['step'] > 10:
                await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                            text='Игра закончена')
                await GameStates.start.set()
            else:
                await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.from_user.id,
                                            text=f'Правильно!\n№: {data["step"]} из 10. Слово: {data["words"]}',
                                            reply_markup=markup)
        else:
            await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.from_user.id,
                                        text=f'Неправильно! попробуйте еще раз\n№: {data["step"]} из 10. Слово: {data["words"]}',
                                        reply_markup=markup)

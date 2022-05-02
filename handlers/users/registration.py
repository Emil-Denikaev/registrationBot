from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Reg


@dp.message_handler(Command("reg"))
async def enter_reg(message: types.Message):
    await message.answer("Вы начали регистрацию.\n"
                         "Пожалуйста, введите фамилию и имя")

    await Reg.Q1.set()


@dp.message_handler(state=Reg.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)
    await message.answer("Введите номер телефона")
    await Reg.next()


@dp.message_handler(state=Reg.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Вы успешно зарегистрировались, наш консультант скоро свяжется с Вами.")
    await message.answer(f"Ваши данные: {answer1}, {answer2}")

    await state.finish()

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from fetch_data import ParseData
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import keyboards as kb

router = Router()


class Reg(StatesGroup):
    description = State()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer('Добро пожаловать ')
    await message.answer('Выберите действие', reply_markup=kb.main)


@router.message(F.text == '/all')
async def get_all_transaction(message: Message, state: FSMContext) -> None:
    transaction_list = await ParseData().get_transaction_json_list()
    if transaction_list is None:
        await message.answer('No transactions')
    for transaction in transaction_list:
        await message.answer(f"""
        id: {transaction['id']}
        method: {transaction['method']}
        amount: {transaction['amount']}
        date: {transaction['date']}
        currency: {transaction['currency']}
        status: {transaction['status']}
        user: {transaction['user']}""")


@router.message(F.text == '/my')
async def take_user_id(message: Message, state: FSMContext) -> None:
    await state.set_state(Reg.description)
    await message.answer('Введите id пользователя')


@router.message(F.text == '/find')
async def take_transaction_is(message: Message, state: FSMContext) -> None:
    await state.set_state(Reg.description)
    await message.answer('Введите id транзакции')


@router.message(Reg.description)
async def get_my_transaction(message: Message, state: FSMContext) -> None:
    await state.update_data(description=message.text)
    data = await state.get_data()
    transaction_list = await (
        ParseData().get_users_transactions_json_list(data["description"])
    )
    if transaction_list is None:
        await message.answer('No transactions')
    for transaction in transaction_list:
        await message.answer(f"""
            id: {transaction['id']}
            method: {transaction['method']}
            amount: {transaction['amount']}
            date: {transaction['date']}
            currency: {transaction['currency']}
            status: {transaction['status']}
            user: {transaction['user']}""")
    await state.clear()


@router.message(Reg.description)
async def get_by_id_transaction(message: Message, state: FSMContext) -> None:
    await state.update_data(description=message.text)
    data = await state.get_data()
    transaction_list = await (
        ParseData().get_transaction_by_id_json_list(data["description"])
    )
    if transaction_list is None:
        await message.answer('No transactions')
    for transaction in transaction_list:
        await message.answer(f"""
            id: {transaction['id']}
            method: {transaction['method']}
            amount: {transaction['amount']}
            date: {transaction['date']}
            currency: {transaction['currency']}
            status: {transaction['status']}
            user: {transaction['user']}""")
    await state.clear()

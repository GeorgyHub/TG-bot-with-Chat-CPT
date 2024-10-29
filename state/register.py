from aiogram.fms.state import StateGroup, State

class RegisterState(StateGroup):
    regName = State()
    regPhone = State()
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMcreate_event(StatesGroup):
  title = State()
  description = State()
  data_start = State()
  data_end = State()
  type = State()
  seats_number = State()


class FSMmake_adm(StatesGroup):
  new_adm = State()
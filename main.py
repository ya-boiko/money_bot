from settings import TOKEN, USERS, DB_NAME
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from Db import Db


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Db(DB_NAME)

db.execute("""
    CREATE TABLE IF NOT EXISTS money_notes(
        note_date TEXT DEFAULT '',
        tg_user_id TEXT DEFAULT '',
        note TEXT DEFAULT ''
    );
""")


@dp.message_handler(commands=['start'])
async def start_menu(msg: types.Message):
    await msg.answer(
        text=f"money money money",
        parse_mode=ParseMode.MARKDOWN
    )


@dp.message_handler(content_types=['text'])
async def get_text_message(msg: types.Message):
    words_list = msg.text.strip().split()
    if str(msg.from_user.id) not in USERS:
        await msg.answer(
            text=f"Ты че пёс охуел 🖕",
            parse_mode=ParseMode.MARKDOWN
        )
        return

    have_nums = False
    for i in words_list:
        if i.isnumeric():
            db.insert(
                query="""
                    INSERT INTO money_notes (
                        note_date,
                        tg_user_id,
                        note
                    ) VALUES (?, ?, ?);
                """,
                data=[(
                    datetime.today().strftime("%d.%m.%Y %H:%M:%S"),
                    msg.from_user.id,
                    msg.text.strip()
                )]
            )
            await msg.answer(
                text=f"Спасибки, записаль ✍️",
                parse_mode=ParseMode.MARKDOWN
            )
            have_nums = True

    if not have_nums:
        await msg.answer(
            text=f"Напиши плиз циферки, а то нихуа не понял 😕",
            parse_mode=ParseMode.MARKDOWN
        )
        return


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

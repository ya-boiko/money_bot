import asyncio
import re

from settings import DB_NAME
from datetime import datetime, timedelta

from Db import Db
from main import send_message_to_users_handler

db = Db(DB_NAME)

today = datetime.today()
tomorrow = today + timedelta(days=1)
result = db.query(
    query=f"""
        select * from money_notes
        where note_date >= '{today.strftime("%d.%m.%Y %H:%M:%S")}' 
        and note_date <= '{tomorrow.strftime("%d.%m.%Y %H:%M:%S")}';
    """
)

users = set([r.get("tg_user_id") for r in result])
spend = {r.get("tg_user_id"): [] for r in result}
get_money = {r.get("tg_user_id"): [] for r in result}
for row in result:
    note = row.get("note")
    numbers = re.findall(r"\d+", row.get("note"))
    if "+" not in note:
        spend.get(row.get("tg_user_id")).extend(numbers)
    else:
        get_money.get(row.get("tg_user_id")).extend(numbers)

text = {r.get("tg_user_id"): "" for r in result}
for user_id in users:
    spend_sum = sum([int(m) for m in spend.get(user_id)])
    get_money_sum = sum([int(m) for m in get_money.get(user_id)])
    text = f"Сегодня мы потратили {spend_sum} щекелей\n\n" \
           f"Сегодня мы заработали {get_money_sum} щекелей"

    asyncio.run(send_message_to_users_handler(user_id, text, True))

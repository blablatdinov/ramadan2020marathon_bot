from bot_init.models import Message


def save_message(msg):
    message_id = msg.message_id
    chat_id = msg.chat.id
    json_str = msg.json
    Message.objects.create(message_id=message_id, chat_id=chat_id, json=json_str)


def create_user(tg_chat_id):
    ...

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def show_channel(client, channel):
    return (
        f'Сообщения в канале должны отправляться раз в **{channel.period}** минут.\n'
        f'Уведомления повторяются **{channel.alert_times}** раз\n'
        f'Выберите действие для **{channel.get_input_channel(client).title}**:\n',
        InlineKeyboardMarkup([
            [InlineKeyboardButton('Удалить 🗑️', f'delete {channel.id}')],
            [InlineKeyboardButton('Запустить ▶' if channel.disabled else 'Остановить ⏸', f'disable {channel.id}')],
            [InlineKeyboardButton('Изменить период отправки 🕒', f'change_period {channel.id}')],
            [InlineKeyboardButton('Изменить количество повторений 🔄', f'change_alerts {channel.id}')],
            [InlineKeyboardButton('Назад к списку каналов 🔙', 'list_channels')],
        ])
    )
def register(app):
    from . import menu, start, messages_in_channels

    menu.register(app)
    start.register(app)
    messages_in_channels.register(app)
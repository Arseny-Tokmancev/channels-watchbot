def register(app):
    from . import list_channel
    list_channel.register(app)

    from . import choose_channel
    choose_channel.register(app)

    from . import functions
    functions.register(app)
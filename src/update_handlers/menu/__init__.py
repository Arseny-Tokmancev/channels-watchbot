def register(app):
    from . import new_channel, my_channels
    new_channel.register(app)
    my_channels.register(app)

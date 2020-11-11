def register(app):
    from . import new_channel, new_channel_command, incoming_channel
    new_channel.register(app)
    new_channel_command.register(app)
    incoming_channel.register(app)
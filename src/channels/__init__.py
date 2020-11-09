def register(app):
    from .new_channel import register as new_channel_register
    new_channel_register(app)
    from .messages_in_channels import register as channel_register
    channel_register(app)
    from .my_channels import register as my_channels_register
    my_channels_register(app)

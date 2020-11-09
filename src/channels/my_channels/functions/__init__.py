def register(app):
    from . import delete, disable, change_period, change_alert
    delete.register(app)
    disable.register(app)
    change_period.register(app)
    change_alert.register(app)
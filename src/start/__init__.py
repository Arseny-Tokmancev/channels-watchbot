def register(app):
    from .start import register as start_register
    start_register(app)
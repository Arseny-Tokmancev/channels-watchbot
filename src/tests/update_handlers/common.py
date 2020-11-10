import unittest


def simple_handler(func):
    return func

class SimpleClient:
    def on_message(self, *_):
        return simple_handler

    def on_callback_query(self, *_):
        return simple_handler

class TestCommon(unittest.TestCase):
    def test_register(self):
        import update_handlers
        try:
            update_handlers.register(SimpleClient())
        except DeprecationWarning:
            pass

def run():
    unittest.main(__name__, exit=False)
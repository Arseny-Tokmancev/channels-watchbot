import unittest
from data.models import Chat


class TestChat(unittest.TestCase):
    def test_create_and_delete(self):
        new_chat = Chat(id=1)
        new_chat.save()
        new_chat = Chat.objects.filter(id=1).first()
        new_chat.delete()


def run():
    unittest.main(__name__, exit=False)
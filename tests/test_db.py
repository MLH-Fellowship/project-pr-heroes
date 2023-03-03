import unittest
from peewee import *
from app import TimelinePost
MODELS = [TimelinePost]
test_db = SqliteDatabase(':memory:')


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe',
                                         email='john@example.com', content='Hellow world, I\'m John!')
        assert first_post.id == 1

        second_post = TimelinePost.create(name='Jane Doe',
                                          email='jane@example.com', content='Hellow world, I\'m Jane!')
        assert second_post.id == 2

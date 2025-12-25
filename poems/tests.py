from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Poem


class PoemTests(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.poem = Poem.objects.create(
            author=cls.user,
            title="A good title",
            body="Somthing string",
        )

    def test_poem_model(self):
        self.assertEqual(self.poem.author.username, "testuser")
        self.assertEqual(self.poem.title, "A good title")
        self.assertEqual(self.poem.body, "Somthing string")
        self.assertEqual(str(self.poem), "A good title (testuser)")


"""
python3 manage.py test
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.222s

OK
Destroying test database for alias 'default'... 
"""

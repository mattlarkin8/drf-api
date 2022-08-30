from django.test import TestCase
from .models import Stuff
from django.contrib.auth import get_user_model

class StuffTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = get_user_model().objects.create_user(username="testuser", password="test")
        testuser.save()

        test_stuff = Stuff.objects.create(name="boat", owner=testuser, description="Water car")
        test_stuff.save()

    def test_stuff_model(self):
        stuff = Stuff.objects.get(id=1)
        actual_owner = str(stuff.owner)
        actual_name = str(stuff.name)
        actual_description = str(stuff.description)
        self.assertEqual(actual_owner, "testuser")
        self.assertEqual(actual_name, "boat")
        self.assertEqual(actual_description, "Water car")
from django.test import TestCase
from django.core.exceptions import ValidationError

from . import models


class FollowerTestCase(TestCase):

    def setUp(self):
        # create users
        models.User.objects.create_user(username="user1", email="user1@email.com", password="MyTesting321654987")
        models.User.objects.create_user(username="user2", email="user2@email.com", password="MyTesting321654987")

    def test_create_user(self):
        user1 = models.User.objects.get(username="user1")
        self.assertEqual(user1.pk, 1)

    def test_follow(self):
        user1 = models.User.objects.get(username="user1")
        user2 = models.User.objects.get(username="user2")
        user1.follower.add(user2)
        self.assertEqual(user1.follower.count(), 1)

    def test_follow_self(self):
        user1 = models.User.objects.get(username="user1")
        user1.follower.add(user1)
        self.assertEqual(user1.follower.count(), 0)

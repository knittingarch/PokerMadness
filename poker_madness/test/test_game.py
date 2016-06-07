from django.test import TestCase
from poker_madness.models import Game

class GameTestCase(TestCase):
    # def setUp(self):
    #     Game.objects.create(state="proposed")

    def test_should_fail_to_start_without_quorum(self):
        self.assertEqual(False, True)
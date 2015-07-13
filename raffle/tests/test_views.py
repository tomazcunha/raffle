# coding: utf-8
from unittest import TestCase
from unittest.mock import patch, Mock

from raffle.models import Raffle
from raffle.views import PickView


class TestPickView(TestCase):

    def setUp(self):
        self.view = PickView
        self.instance = PickView()

    def test_view_uses_correct_template(self):
        self.assertEqual(u'templates/pick.html', self.instance.template)

    def test_view_uses_correct_model(self):
        self.assertEqual(u'Raffle', self.instance.model.__name__)

    def test_view_initializes_raffle_instance(self):
        instance = PickView()
        self.assertIsInstance(instance.raffle, Raffle)

    @patch('builtins.next', Mock())
    def test_view_post_calls_next_item_from_raffle(self):
        self.instance.post()
        self.assertTrue(next.called)

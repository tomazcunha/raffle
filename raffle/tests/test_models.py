# coding: utf-8
from unittest import TestCase

from raffle.models import Raffle


class TestRaffle(TestCase):

    def setUp(self):
        self.model = Raffle
        self.instance = self.model([u'a', u'b', u'c'])

    def test_initializes_raffle_correctly(self):
        instance = self.model([u'a', u'b', u'c'])
        self.assertIn(u'a', instance.items)
        self.assertIn(u'b', instance.items)
        self.assertIn(u'c', instance.items)
        self.assertEqual(3, len(instance.items))

    def test_next_push_item_from_list(self):
        raffled_item = next(self.instance)
        self.assertNotIn(raffled_item, self.instance.items)

    def test_next_raises_error_if_raffle_has_no_more_items(self):
        instance = self.model([])
        self.assertRaises(StopIteration, next, instance)

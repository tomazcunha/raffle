# coding: utf-8
import random


class Raffle:

    def __init__(self, items):
        self.items = items
        random.shuffle(self.items)

    def __iter__(self):
        return (item for item in self.items)

    def __next__(self):
        try:
            return self.items.pop(0)
        except IndexError:
            raise StopIteration

# coding: utf-8
from raffle.models import Raffle


class PickView:

    model = Raffle
    template = u'templates/pick.html'

    def __init__(self):
        self.raffle = Raffle([u'a', u'b', u'c'])

    def post(self):
        return next(self.raffle)

# -*- coding: utf-8 -*-
from datetime import date

from easydict import easy_dict

__author__ = 'banxi'


def test_easy_dict():
    book_dict = {
        'title': 'David Copperfield',
        'characters': [
            'David Copperfield',
            'Clara Copperfield',
            'Clara Peggotty',
            'Betsey Trotwood',
            'Anges Wickfield',
            'Dora Spenlow'
        ],
        'author': {
            'first_name': 'Dickens',
            'last_name': 'Charles',
            'birth': date(1812, 2, 7),
        }
    }

    bd = easy_dict(book_dict)

    assert bd.author.first_name == 'Dickens'
    assert bd.author.birth == date(1812, 2, 7)
    assert bd.characters[0] == 'David Copperfield'
    assert bd.non_exists_key is None


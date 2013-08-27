#!/usr/bin/python2.7
'''rps.py simulates a never-ending game of rock, paper scissor between two players'''

from threading import Thread
from Queue import Queue
import time
import random


class Hand(object):
    '''Represents a sign choice'''
    def __init__(self, choice):
        self.choice = choice
        self._winners = {
            'rock': 'scissor',
            'paper': 'rock',
            'scissor': 'paper',
        }

    def __str__(self):
        return self.choice

    def __eq__(self, other_hand):
        return self.choice == other_hand.choice

    def __gt__(self, other_hand):
        return self._winners[self.choice] == other_hand.choice

    def __lt__(self, other_hand):
        return self._winners[other_hand.choice] == self.choice


def _player_thread(my_queue):
    while True:
        time.sleep(random.randint(0, 3))  # Thinking about next move
        my_queue.put(Hand(random.choice(['rock', 'paper', 'scissor'])))


def _ref_thread(queue_1, queue_2):
    _round = 0
    results = []
    while True:
        _round += 1
        print 'Round {}. Waiting for players to choose'.format(_round)
        choice_1 = queue_1.get()
        choice_2 = queue_2.get()
        if choice_1 > choice_2:
            message = 'Player 1 wins'
            results.append(1)
        elif choice_1 < choice_2:
            message = 'Player 2 wins'
            results.append(2)
        else:
            message = 'It\'s a tie'
            results.append(3)
        print '{}\t {} vs {}'.format(message, choice_1, choice_2)
        print 'Player 1 total: {}, Player 2 total: {}, Ties: {}\n'.format(
            results.count(1), results.count(2), results.count(3))


def _start_thread(func, args):
    t = Thread(target=func, args=args)
    t.daemon = True
    t.start()


def play(time_limit=60):
    player_queues = [Queue()] * 2
    _start_thread(_ref_thread, player_queues)
    for _id in range(2):
        _start_thread(_player_thread, (player_queues[_id],))
    time.sleep(time_limit)
    print 'Game Over'


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print 'Game Over'

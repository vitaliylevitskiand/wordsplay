import time
import game

request_time_expiration = 120
game_requests = {}
move_time_cases = [120, 60, 45, 30, 15]
games = {}


class GameRequest(object):
    def __init__(self, user, move_time):
        self.user = user
        self.move_time = move_time
        self.created_at = time.time()


def create_game_request(user, move_time):
    game_request = GameRequest(user, move_time)
    game_requests[user.id] = game_request


def cencel_game_request(user):
    del game_requests[user.id]


def get_game_requests(user):
    return game_requests


def start_game(user1, user2):
    new_game = game.Words([user1.username, user2.username], 5, 'ua')
    return new_game.board



def apply_request(applier, user_id):
    game_request = game_requests[user_id]
    if not game_request:
        raise Exception('No such game request with user with id %s!' % user_id)
    start_game(game_requests[user_id].user, applier)
    del game_requests[game_requests]

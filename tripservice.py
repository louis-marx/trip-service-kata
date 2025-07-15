#!/usr/bin/env python


#
# Exceptions
#
class DependendClassCallDuringUnitTestException(Exception):
    pass

class UserNotLoggedInException(Exception):
    pass

#
# Classes
#
class Trip:
    pass

class User:
    def __init__(self):
        self.trips = []
        self.friends = []

    def add_friend(self, user):
        self.friends.append(user)

    def add_trip(self, trip):
        self.trips.append(trip)

    def get_friends(self):
        return self.friends

#
# Dependencies
#
def _is_user_logged_in(user: User):
    raise DependendClassCallDuringUnitTestException(
        "_isUserLoggedIn() should not be called in an unit test"
    )

def _get_logged_user():
    raise DependendClassCallDuringUnitTestException(
        "_getLoggedUser() should not be called in an unit test"
    )

def _find_trips_by_user(user: User):
    raise DependendClassCallDuringUnitTestException(
        "_findTripsByUser() should not be invoked on an unit test."
    )

#
# TripService Class
#
class TripService:
    def get_trips_by_user(self, user: User):
        logged_user = self.get_logged_user()
        if logged_user:
            if logged_user in user.get_friends():
                return _find_trips_by_user(user)
            else:
                return []
        else:
            raise UserNotLoggedInException()

    def get_logged_user(self):
        return _get_logged_user()


if __name__ == "__main__":
    pass
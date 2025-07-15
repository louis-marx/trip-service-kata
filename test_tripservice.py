from tripservice import User, UserNotLoggedInException, TripService
import pytest


class TestTripService:

    def test_should_throw_an_exception_when_user_is_not_logged_in(self, monkeypatch):
        trip_service = TripService()
        user = User()
        monkeypatch.setattr("tripservice._get_logged_user", lambda: None)
        with pytest.raises(UserNotLoggedInException):
            trip_service.get_trips_by_user(user)
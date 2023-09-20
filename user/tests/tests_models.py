from django.test import TestCase
from user.models import Users, UserDetails, UserPreference

class UsersTest(TestCase):
    """ Test module for User model """

    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()

    def setUp(self) -> None:
        Users.objects.create(
            country_code="+91",
            mobile_number=9883725994,
            user_name="python"
        )
        Users.objects.create(
            country_code="+91",
            mobile_number=9883725995,
            user_name="cobra"
        )
        return super().setUp()
    

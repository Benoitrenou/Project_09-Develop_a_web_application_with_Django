from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from reviews.models import UserFollow


class User(AbstractUser):
    """ Class of User
    """
    def get_connections(self):
        """ Method which returns users that the user follows
        """
        connections = UserFollow.objects.filter(
            Q(user=self)
        )
        return [connection.followed_user for connection in connections]

    def get_followers(self):
        """ Method which returns users who follows the user
        """
        followers = UserFollow.objects.filter(
            Q(followed_user=self)
        )
        return [follower.user for follower in followers]

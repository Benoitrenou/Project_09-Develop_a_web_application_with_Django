from django.contrib.auth.models import AbstractUser
from reviews.models import UserFollows
from django.db.models import Q

class User(AbstractUser):
    def get_connections(self):
        connections = UserFollows.objects.filter(
            Q(user=self)
        )
        return [connection.followed_user for connection in connections]

    def get_followers(self):
        followers = UserFollows.objects.filter(
            Q(followed_user=self)
        )
        return [follower.user for follower in followers]

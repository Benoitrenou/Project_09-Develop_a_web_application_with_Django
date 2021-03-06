from django import template
from django.utils import timezone

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

register = template.Library()


@register.filter
def model_type(value):
    """ Creates a template filter
    returning the name of type of value
    """
    return type(value).__name__


@register.simple_tag
def in_range(number):
    """ Creates a template tag returning an iterable
    of the length given of the number in argument
    """
    number = abs(number)
    return [*range(number)]


@register.filter
def get_posted_at_display(posted_at):
    """ Creates a template filter
    adaptating the display of time_created attribute
    """
    seconds_ago = (timezone.now() - posted_at).total_seconds()
    if seconds_ago <= HOUR:
        return f'Publié il y a {int(seconds_ago // MINUTE)} minutes.'
    elif seconds_ago <= DAY:
        return f'Publié il y a {int(seconds_ago // HOUR)} heures.'
    return f'Publié le {posted_at.strftime("%d %b %y à %Hh%M")}'


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    """ Creates a template filter
    adaptating the display of user attribute
    """
    if user == context['user']:
        return 'vous'
    return user.username

import re

from django import template
from django.urls import NoReverseMatch, reverse
from Insta.models import Like, Post


register = template.Library()


@register.simple_tag
def is_following(current_user, background_user):
    return background_user.get_followers().filter(creator=current_user).exists()


@register.simple_tag
def has_user_liked_post(post, user):
    try:
        Like.objects.get(post=post, user=user)
        return "fas"
    except:
        return "far"


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''
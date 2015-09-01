# -*- encoding: utf-8 -*-

from django import template

register = template.Library()

LANGUAGES = {'es': 'Español', 'en': 'English'}


def language_name(value):
	return LANGUAGES[value]

register.filter('language_name', language_name)

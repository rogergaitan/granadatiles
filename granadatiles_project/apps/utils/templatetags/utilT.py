__author__ = 'ervingbonilla'
from django import template

register = template.Library()

LANGUAGES = {'es': 'Espanol', 'pt': 'Portugues', 'en': 'English'}

def language_name(value):
	return LANGUAGES[value]

register.filter('language_name', language_name)

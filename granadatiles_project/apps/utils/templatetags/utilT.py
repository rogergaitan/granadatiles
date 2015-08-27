#-*- encoding: utf-8 -*-
__author__ = 'ervingbonilla'
from django import template

register = template.Library()

LANGUAGES = {'es': 'Español', 'pt': 'Português', 'en': 'English'}

def language_name(value):
	return LANGUAGES[value]

register.filter('language_name', language_name)

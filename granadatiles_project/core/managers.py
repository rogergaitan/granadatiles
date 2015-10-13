from django.db import models
from _datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist


class BaseSlugManager(models.Manager):

    def get_id(self, slug, language):
        if language == 'es':
            try:
                id = self.get(slug_es=slug).id
            except ObjectDoesNotExist:
                id = self.get(slug=slug).id
        else:
            id = self.get(slug=slug).id
        return id


class BaseDateManager(models.Manager):

    def available_years(self):
        years = self.dates('date', 'year', order='DESC')
        return years

    def available_months(self, year):
        months = self.filter(date__year=year).dates(
            'date', 'month', order='DESC')
        return months

    def available_years_datetime(self):
        years = self.datetimes('date', 'year', order='DESC')
        return years

    def available_months_datetime(self, year):
        months = self.filter(date__year=year).datetimes(
            'date', 'month', order='DESC')
        return months

    def get_by_date(self, month, year):
        return self.filter(date__month=month, date__year=year).order_by('-date')

    def get_by_trimesters(self, year, trimester):
        min_date = datetime(year, min(trimester), 1)
        max_date = datetime(year, max(trimester)+1, 1)
        DD = timedelta(days=1)
        max_date = max_date - DD
        return self.filter(date__gte=min_date, date__lte=max_date).order_by('-date')

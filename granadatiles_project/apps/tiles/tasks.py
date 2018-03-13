from __future__ import absolute_import

from django.core.management import call_command

from celery import shared_task

@shared_task()
def update_inventory_task():
    call_command('update_inventory')

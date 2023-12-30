# tasks.py
from celery import shared_task
import asyncio
import os
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Task, TaskStatus
from karma_bean.celery import app
from celery.schedules import crontab
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.messages import SendMessageRequest
@shared_task
def update_task_status():
    now = timezone.now()

    # Find tasks with deadline + 3 days that have status 'REVIEW'
    tasks_to_reject = Task.objects.filter(
        deadline__lte=now + timedelta(days=3),
        deadline__gt=now,
        status=TaskStatus.REVIEW.value
    )

    # Update status to 'REJECT', if user lazy not to review will be punished by auto reject
    tasks_to_reject.update(status=TaskStatus.REJECT.value)

    

@shared_task
def send_notification():
    # Get tasks with a deadline set for tomorrow
    tomorrow_deadline_tasks = Task.objects.filter(
        deadline__date=(timezone.now() + timedelta(days=1)).date(),
    )

    # Send notification at 10pm the day before the deadline
    
    ret = "Notification deadline task: \n"    
    for task in tomorrow_deadline_tasks:
        # Assuming the notification is sent using some notification service
        # Replace the following line with your notification logic
        ret +=send_notification_logic(task)
    

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    
    app_id = os.getenv('app_id')
    hash_ = os.getenv('hash_')
    client = TelegramClient(
        'anon',
        app_id,
        hash_
    )
    # Start the client
    bot_token = os.getenv('bot_token')
    client.start(bot_token=bot_token)
    print("Client Created")
    channel_id = int(os.getenv('channel_id'))
    async def send_mess(message):
        await client.send_message(channel_id, message=message)
    with client:
        client.loop.run_until_complete(send_mess(message=ret))


    
        

def send_notification_logic(task):
    # Replace this with your actual notification logic
    ret = f"id {task.id} task: {task.name}, Deadline: {task.deadline} \n"
    print(ret)
    return ret
    # Your notification logic goes here


app.conf.beat_schedule["change task review to reject"] = {
    "task": "karma_bean.tasks.tasks.update_task_status",
    "schedule": crontab(hour=21, minute=0),
    # "schedule": crontab(minute="*/1"),
}

app.conf.beat_schedule["noti deadline"] = {
    "task": "karma_bean.tasks.tasks.send_notification",
    "schedule": crontab(hour=20, minute=0),
    # "schedule": crontab(minute="*/1"),
}
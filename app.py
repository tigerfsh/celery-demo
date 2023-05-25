from celery import Celery
from celery.schedules import crontab
from urllib.parse import quote 

redis_password = "tASDF1@#f7V55QpuVHI"
redis_password = quote(redis_password)

app= Celery(broker=f"redis://:{redis_password}@10.206.128.104:30510/0", backend=f"redis://:{redis_password}@10.206.128.104:30510/1")

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)

@app.task
def add(x, y):
    z = x + y
    print(z)

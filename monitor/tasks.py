from  .celery.utils import  register_as_period_task
from celery import shared_task
from django.conf import  settings
import redis

#  使用redis连接池 操作
Pool = redis.ConnectionPool(host =settings.REDIS_HOST,port=settings.REDIS_PORT, max_connections=30)


@shared_task
@register_as_period_task(crontab ="* * * * *",interval =10)
def  init_task():
    conn = redis.Redis(connection_pool=Pool)
    pipe = conn.pipeline()
    flag =pipe.lpush(settings.REDIS_KEY,'https://www.baidu.com/')
    print(flag)
    pipe.execute()
    print('hello redis')






















#  一些model 以后可能会用到

from django.db import models
import datetime

#  域名监控系统
class Scraper(models.Model):
    STATUS_CHOICES = (
        ('A', 'ACTIVE'),
        ('M', 'MANUAL'),
        ('P', 'PAUSED'),
        ('I', 'INACTIVE'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    help_text = "Runtime status of the scraper, used by scheduling mechanism."
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P', help_text=help_text)


class SchedulerRuntime(models.Model):
    TYPE = (
        ('S', 'SCRAPER'),
        ('C', 'CHECKER'),
    )
    id = models.AutoField(primary_key=True)
    runtime_type = models.CharField(max_length=1, choices=TYPE, default='P')
    next_action_time = models.DateTimeField(default=datetime.datetime.now)
    next_action_factor = models.FloatField(default="")
    num_zero_actions = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


#  默认用redis 做scheduler
class Scheduler(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    redis_key =  models.CharField(max_length=20,default='',blank=False,null=False)



class WebSite(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, null=True, on_delete=models.SET_NULL)
    scheduler = models.ManyToManyField(Scheduler,  null=True)
    note = models.TextField(default="")
    status = models.IntegerField(default=1)


class  DomainDnsinfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,blank=False,null=False,default="")
    A_record =  models.CharField(max_length=30,blank=False,null=False,default="")
    Mx_record = models.CharField(max_length=30,blank=False,null=False,default="")
    status =  models.IntegerField(default=1,null=False)
    website = models.ManyToManyField(WebSite,null=True)
















#














#  接下来就是增删改查了 找个框架  bs3











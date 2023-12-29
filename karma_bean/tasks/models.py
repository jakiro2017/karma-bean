from django.db import models
from django.utils.translation import gettext_lazy as _
class TaskStatus(models.TextChoices):
    BOOKED = "BOOKED", _("BOOKED")
    DOING = "DOING", _("DOING")    
    REVIEW = "REVIEW", _("REVIEW")
    REJECT = "REJECT", _("REJECT")
    DONE = "DONE", _("DONE")
# Create your models here.
class SpendPoint(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=100)
    explaination = models.TextField()
    generic_demand = models.FloatField()
    isIncome = models.BooleanField()

    def __str__(self):
        return self.code

    class Meta:
        managed = True
        verbose_name = "SpendPoint"
        verbose_name_plural = "SpendPoints"


class Task(models.Model):
    name = models.CharField(max_length=500)
    status = models.CharField(
        max_length=30,
        choices=TaskStatus.choices,
        default=TaskStatus.BOOKED,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.ForeignKey(SpendPoint, on_delete=models.PROTECT)
    base_point = models.IntegerField()
    base_point_predict = models.IntegerField(blank=True, null=True)
    base_point_penalty_if_fail = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    note_prediction = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

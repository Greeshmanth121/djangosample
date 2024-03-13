from django.db import models

class student(models.Model):
    sname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    fees = models.CharField(max_length=100)

    class meta:
        db_table = 'student'

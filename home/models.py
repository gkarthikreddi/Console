from django.db import models


class Loan(models.Model):
    user = models.CharField(max_length=12)
    name = models.CharField(max_length=20)
    tenure = models.IntegerField()
    emi = models.DecimalField(max_digits=8, decimal_places=2)
    start = models.DateField()


class Expense(models.Model):
    user = models.CharField(max_length=12)
    yyyymm = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    utilities = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    food = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    groceries = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    shoping = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fuel = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subscriptions = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    emis = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    something = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    msg = models.CharField(max_length=40, default="0")


class Investment(models.Model):
    user = models.CharField(max_length=12)
    yyyymm = models.IntegerField()
    stocks = models.DecimalField(max_digits=12, decimal_places=2)
    mf = models.DecimalField(max_digits=12, decimal_places=2)
    gold = models.DecimalField(max_digits=12, decimal_places=2)
    assets = models.DecimalField(max_digits=12, decimal_places=2)

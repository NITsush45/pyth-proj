from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=49)

    def __str__(self):
        return self.name

class Branch(models.Model):
    ifsc = models.CharField(max_length=200)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name=models.CharField(max_length=74)

    def __str__(self):
        return self.branch


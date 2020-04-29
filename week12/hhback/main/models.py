from django.db import models

class Company (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    city = models.CharField(max_length=100)
    address = models.TextField(default='')

    def short_jsn(self):
        return {
            'id': self.id,
            'city': self.city,
        }

    def full_jsn(self):
        return {
            'id': self.id,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def short_jsn(self):
        return {
            'id': self.id,
            'salary': self.salary,
        }

    def full_jsn(self):
        return {
            'id': self.id,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.full_jsn(),
        }
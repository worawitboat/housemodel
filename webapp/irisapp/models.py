from django.db import models

# Create your models here.
class Species(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Feature(models.Model):
    fid = models.AutoField(primary_key=True)
    # กลีบหลัก
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    # กลีบรอง
    petal_length = models.FloatField()
    petal_width = models.FloatField()

    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    def __str__(self):
        return str([
            self.sepal_length, self.sepal_width,
            self.petal_length, self.petal_width
        ])

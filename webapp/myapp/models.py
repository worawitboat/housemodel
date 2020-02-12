from django.db import models

# Create your models here.assi
class PrimeMinister(models.Model):
    # fields
    # - pid (pid) 
    pid = models.AutoField(primary_key=True)
    # - ชื่อ (name) 
    name = models.CharField(max_length=500)
    # - วันเดือนปีเกิด (dob)
    dob = models.DateField()
    # - วันที่รับตำแหน่ง (startdate)
    startdate = models.DateField()
    # - วันที่พ้นตำแหน่ง (enddate)
    enddate = models.DateField()
    # - รูป url (imageurl)
    imgurl = models.CharField(max_length=500, default='')
    # - พรรค (party)
    party = models.CharField(max_length=500, default='')
    # constructor
    # methods
    def __str__(self):
        return f'{self.name} จากพรรค {self.party}'
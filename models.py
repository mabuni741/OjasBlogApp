from django.db import models
from django.contrib.auth.models import User


class employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    state = models.CharField(max_length=25,blank=True)


    def __str__(self):
        return self.name
       
       
       
    class Meta:
        db_table='Employee Details'


# class emp_data(models.Model):
#     emp_salary = models.CharField(max_length=20)
#     emp_section = models.CharField(max_length=7)
#     emp = models.ForeignKey(employee,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.emp_salary

#     class Meta:
#         db_table = 'emp_personal_details'                



# class Personal(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
#     name = models.CharField(max_length=20)
#     email = models.CharField(max_length=25)
#     mobile=models.CharField(max_length=10)
#     pic = models.FileField(upload_to='media/') 
#     otp = models.CharField(max_length=6,default='00000')

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table='personal'    


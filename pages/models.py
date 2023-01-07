from django.db import models

# Create your models here.
# class Car(models.Model):
#     years = [("2013","2013"),("2014","2014"),("2015","2015")] #=>year w7da htzhrli w w7da htt7t fe database
#     name = models.CharField(max_length=50 , default="car",  verbose_name="Title") #=>verbose 3shan yzhr f admin page asmha title
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     color = models.CharField(max_length=20)
#     image = models.ImageField(upload_to='photos/%y/%m/%d')
#     description = models.TextField(null = True , blank= True) #=>lw md5lsh input htkon null
#     model = models.CharField(default="default", choices=years , max_length=50) #=> option for models
#     def __str__(self):  #=> must return a string 
#        return self.name  #=> 3shan t5li car tzhr b2smha msh id
#     #    return str(self.price)
#     class Meta:
#         ordering = ['name'] #=> order ascending 
#         # ordering = ['-name'] #=> order descending 
#         verbose_name = "my car" #=> asm class f admin page


# Create your models here.
class Project(models.Model):
    options= [("Art","Art"),("Design","Design"),("Food","Food"),("Games","Games")] #=>year w7da htzhrli w w7da htt7t fe database
    name = models.CharField(max_length=50 , default="project",  verbose_name="Project Title") #=>verbose 3shan yzhr f admin page asmha title
    current_situation = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(blank= True,upload_to='photos/%y/%m/%d')
    description = models.TextField(null = True , blank= True) #=>lw md5lsh input htkon null
    category = models.CharField(default="default", choices=options , max_length=50) #=> option for models
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    def __str__(self):  #=> must return a string 
       return self.name  #=> 3shan t5li car tzhr b2smha msh id
    #    return str(self.price)
    class Meta:
        ordering = ['name'] #=> order ascending 
        # ordering = ['-name'] #=> order descending 
        verbose_name = "Project" #=> asm class f admin page



class Employee(models.Model):
    name = models.CharField(max_length = 50 )
    age = models.IntegerField()
    # relation = models.OneToOneField(Car , on_delete = models.PROTECT, null=True,blank=True) #=> lw ms7t employee, car mwgoda 
    # relation = models.OneToOneField(Car , on_delete = models.CASCADE, null=True,blank=True) #=> lw ms7t employee, car mwgoda 
    cars = models.ManyToManyField(Project)
    def __str__(self):
        return self.name  
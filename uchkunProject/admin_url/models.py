from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class University(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name    

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    stud_id = models.CharField(max_length=100, unique=True)  # Убедитесь, что поле stud_id существует
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    essential = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    
class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"



class Grades(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.grade}"
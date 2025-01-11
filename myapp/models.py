from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title


class UserInformation(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    GOAL_CHOICES = [
        ('WL', 'Weight Loss'),
        ('MG', 'Muscle Gain'),
        ('SF', 'Stay Fit'),
        ('IM', 'Improve Mobility')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    fitness_goal = models.CharField(max_length=2, choices=GOAL_CHOICES)
    medical_conditions = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_bmi(self):
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters ** 2), 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def __str__(self):
        return f"{self.user.username}'s Information"

    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = "User Information"
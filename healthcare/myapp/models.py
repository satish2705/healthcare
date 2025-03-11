from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# activity profile starts

ACTIVITY_CHOICES = [
    ('login', 'Login'),
    ('logout', 'Logout'),
    ('purchase', 'Purchase'),
    ('comment', 'Comment'),
]

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100, choices=ACTIVITY_CHOICES)
    activity_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_activity_type_display()} at {self.activity_time}"

# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     activity_type = models.CharField(max_length=100)
#     activity_time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.activity_type} at {self.activity_time}"
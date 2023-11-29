from django.db import models

class Pereval(models.Model):
    new = 'New'
    pending = 'Pending'
    accepted = 'Accepted'
    rejected = 'Rejected'
    result_status = [('new', 'New'), ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'),]

    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user_email = models.EmailField()
    user_fam = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_otc = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    height = models.IntegerField()
    winter_level = models.CharField(max_length=10, blank=True)
    summer_level = models.CharField(max_length=10, blank=True)
    autumn_level = models.CharField(max_length=10, blank=True)
    spring_level = models.CharField(max_length=10, blank=True)
    status = models.CharField(max_length=20, choices=result_status, default='new')


class Image(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    data = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)

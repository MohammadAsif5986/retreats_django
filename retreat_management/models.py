from django.db import models

class Retreat(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=20)
    retreat = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    payment_details = models.TextField()
    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_id', 'retreat')

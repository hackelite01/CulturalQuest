# your_app_name/models.py
from django.db import models
from django.utils.safestring import mark_safe

class User(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ECimage = models.ImageField(upload_to='event_categories/', blank=True, null=True)

    def __str__(self):
        return self.name

    def EC_image(self):
        if self.ECimage:
            return mark_safe('<img src="{}" width="100"/>'.format(self.ECimage.url))
        return '-'
    EC_image.short_description = 'Image Preview'


class Event(models.Model):
    title = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='events_as_title')
    description = models.TextField()
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='events_as_category')
    venue_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    Eimage = models.ImageField(upload_to='events/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title.name
    
    def E_image(self):
        if self.Eimage:
            return mark_safe('<img src="{}" width="100"/>'.format(self.Eimage.url))
        return '-'
    E_image.short_description = 'Event Image Preview'
    


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participants = models.PositiveIntegerField()
    booking_date = models.DateField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ), default='pending')

    def __str__(self):
        return f"{self.user.name} - {self.event.title}"


class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=(
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('cash', 'Cash'),
        ('other', 'Other'),
    ))
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ), default='pending')

    def __str__(self):
        return f"Payment for Booking ID: {self.booking.id}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.name} for {self.event.title}"


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

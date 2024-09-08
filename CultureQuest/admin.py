# your_app_name/admin.py
from django.contrib import admin
from .models import User, Country, State, City, EventCategory, Event, Booking, Payment, Review, ContactUs
from django.utils.safestring import mark_safe

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    search_fields = ['name']

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'EC_image']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'venue_name', 'date', 'time_from', 'time_to', 'city', 'state', 'country', 'E_image']
    list_filter = ['date', 'city', 'state', 'country']
    search_fields = ['title', 'venue_name', 'description']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'participants', 'booking_date', 'status']
    list_filter = ['status', 'booking_date']
    search_fields = ['user__name', 'event__title']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['booking', 'user', 'amount', 'payment_date', 'payment_method', 'status']
    list_filter = ['payment_date', 'payment_method', 'status']
    search_fields = ['user__name', 'booking__event__title']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'rating', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__name', 'event__title']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email', 'phone']


from django.contrib import admin
from .models import Rating
# RATING ADMIN
class RatingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rating._meta.fields]

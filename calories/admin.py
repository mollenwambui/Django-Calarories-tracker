from django.contrib import admin
from .models import Food,PostFood,Profile
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
admin.site.register(Food)
admin.site.register(Profile)

# Register your models here.

from django.contrib import admin
from .models import User
#from django.contrib.auth.admin import UserAdmin

# Now register the new User
admin.site.register(User)



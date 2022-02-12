from django.contrib import admin

from doctors.models import Doctor,Review,Special

admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(Special)

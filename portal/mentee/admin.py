from django.contrib import admin
from .models import mentee, mentor, interview, feedback
# Register your models here.

admin.site.register(mentee)
admin.site.register(mentor)
admin.site.register(interview)
admin.site.register(feedback)
from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Teachers)
from django.contrib import admin
from application import models

admin.site.register(models.Profile)
admin.site.register(models.TagQuestion)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.LikeQuestion)
admin.site.register(models.LikeAnswer)



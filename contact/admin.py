from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'topic', 'content']

    class Meta:
        model = Feedback

admin.site.register(Feedback,FeedbackAdmin)

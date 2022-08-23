from django.contrib import admin
from django.contrib.auth import get_user_model
from leads.models import Agent, Lead

User = get_user_model()

admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(User)

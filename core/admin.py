# core/admin.py
from django.contrib import admin
from .models import MensagemFeedback

@admin.register(MensagemFeedback)
class MensagemFeedbackAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio')
    list_filter = ('data_envio',)
    search_fields = ('nome', 'email', 'mensagem')
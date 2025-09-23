# core/models.py
from django.db import models

class MensagemFeedback(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True, help_text="Nome (opcional)")
    email = models.EmailField(blank=True, null=True, help_text="Email (opcional, para contato)")
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome or 'Anônimo'} - {self.data_envio.strftime('%d/%m/%Y %H:%M')}"
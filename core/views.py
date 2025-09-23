# core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages # Importe messages
from .forms import FeedbackForm

def pagina_contato(request):
    # Dicionário com as informações estáticas de contato do seu protótipo
    info_contato = {
        'telefone': '+1 (123) 1231-1233',
        'instagram': '@sushiemcasausa',
        'email': 'sushiemacasausa@gmail.com',
        'whatsapp': '+1 (123) 1231-1233'
    }

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu feedback foi enviado com sucesso! Obrigado.') # Mensagem de sucesso
            return redirect('contato') # Redireciona para a mesma página (limpa o formulário)
    else:
        form = FeedbackForm()

    context = {
        'form': form,
        'info_contato': info_contato
    }
    return render(request, 'core/contato.html', context)
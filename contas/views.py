from django.shortcuts import render
from .models import Transacao
import datetime

def home(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'contas/home.html')

def listagem(request):
	data = {}
	data['transacoes'] = Transacao.objects.all()
	return render(request, 'contas/listagem.html', data)
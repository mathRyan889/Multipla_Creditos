from django.shortcuts import render, redirect
from .forms import RegisterLeadForm

def home(request):
    if request.method == 'POST':
        form = RegisterLeadForm(request.POST)
        if form.is_valid():
            form.save()
            # O redirect é essencial para limpar o form e recarregar a lista do banco
            return redirect('home') 
    else:
        form = RegisterLeadForm()
    
    return render(request, 'home.html', {'form': form})

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')
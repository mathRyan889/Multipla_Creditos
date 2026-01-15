from django.shortcuts import render
from .forms import RegisterLeadForm

def home(request):
    if request.method == 'POST':
        form = RegisterLeadForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = RegisterLeadForm()
    
    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')

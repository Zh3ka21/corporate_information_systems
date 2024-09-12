
from django.shortcuts import render, redirect
from .forms import CssForm
from .models import CssParameters

def index(request):
    return render(request, 'tasks/index.html')


def task2(request):
    paragraph_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'  
    text_color = 'black' 
    background_color = 'white'
    css_params = CssParameters.objects.first() 

    if request.method == 'POST':
        form = CssForm(request.POST)
        if form.is_valid():
            # Get the user input
            paragraph_text = form.cleaned_data['paragraph_text'] or paragraph_text
            text_color = form.cleaned_data['text_color'] or text_color
            background_color = form.cleaned_data['background_color'] or background_color
    else:
        form = CssForm()

    return render(request, 'tasks/task2.html', {
        'form': form,
        'paragraph_text': paragraph_text,
        'text_color': text_color,
        'background_color': background_color,
        'css_params': css_params,
    })
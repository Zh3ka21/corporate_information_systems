
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CssForm
from .models import CssParameters, Image

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

def task3_success(request):
    return render(request, 'tasks/task3_success.html')

def task3_error(request):
    return render(request, 'tasks/task3_error.html')

def task3(request):
    if request.method == 'POST':
        image_data = request.POST.get('images[]')
        if image_data:
            # Split the data by '|' to get each URL-height pair
            image_pairs = image_data.split('|')
            # Clear existing entries if needed
            Image.objects.all().delete()
            for pair in image_pairs:
                url, height = pair.split(',')
                Image.objects.create(url=url, height=int(height))
            return redirect(reverse('task3_success'))  # Redirect to a success page
        return redirect(reverse('task3_error'))  # Redirect to an error page if no data
    return render(request, 'tasks/task3.html')
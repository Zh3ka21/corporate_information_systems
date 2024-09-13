
from django.db import IntegrityError
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
            image_pairs = image_data.split('|')
            
            # Ensure at least 5 images
            current_images = Image.objects.all()
            if current_images.count() > 5:
                keep_ids = current_images.order_by('-id')[:5].values_list('id', flat=True)
                to_delete = current_images.exclude(id__in=keep_ids)
                to_delete.delete()

            for pair in image_pairs:
                url, height_str = pair.split(',')
                try:
                    height = int(height_str)
                    image, created = Image.objects.update_or_create(
                        url=url,
                        defaults={'height': height}
                    )
                except ValueError:
                    height = 0
                except IntegrityError:
                    raise IntegrityError("Such image exist.")
            
            return redirect(reverse('task3_success'))
        return redirect(reverse('task3_error'))

    sizes = Image.objects.all()
    return render(request, 'tasks/task3.html', {'sizes': sizes})

def task4_success(request):
    return render(request, 'tasks/task3_success.html')

def task4_error(request):
    return render(request, 'tasks/task3_error.html')

def task4(request):
    if request.method == 'POST':
        image_data = request.POST.get('images[]')
        if image_data:
            image_pairs = image_data.split('|')
            
            # Ensure at least 5 images
            current_images = Image.objects.all()
            if current_images.count() > 5:
                keep_ids = current_images.order_by('-id')[:5].values_list('id', flat=True)
                to_delete = current_images.exclude(id__in=keep_ids)
                to_delete.delete()

            for pair in image_pairs:
                url, height_str = pair.split(',')
                try:
                    height = int(height_str)
                    image, created = Image.objects.update_or_create(
                        url=url,
                        defaults={'height': height}
                    )
                except ValueError:
                    height = 0
                except IntegrityError:
                    raise IntegrityError("Such image exist.")
            
            return redirect(reverse('task3_success'))
        return redirect(reverse('task3_error'))

    urls = Image.objects.all()
    return render(request, 'tasks/task4.html', {'urls': urls[0:3]})
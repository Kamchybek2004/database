from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.conf import settings
import requests

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})


# Функция для подключения REST API
def get_weather_data(request):
    url = "http://api.openweathermap.org/data/2.5/weather"

    city = request.GET.get('city', 'Bishkek')
    params = {
        "q": city,
        "appid": settings.WEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_data = response.json()
    except requests.exceptions.HTTPError as http_err:
        weather_data = f"HTTP error occured: {http_err}"
    except Exception as err:
        weather_data = f"Other error occurred: {err}"

    return render(request, 'book_list.html', {'weather_data': weather_data})
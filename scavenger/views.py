from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse  

# Create your views here.

def splash_screen(request):
    return render(request, 'splash.html')

def main_page(request):
    if request.method == 'POST':
        decodedText = request.POST.get('decodedText')
        return JsonResponse({'success': True})

    return render(request, 'index.html')

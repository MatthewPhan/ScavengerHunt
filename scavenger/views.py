from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'index.html')

def splash_screen(request):
    return render(request, 'splash.html')
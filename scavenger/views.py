import json

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.

def splash_screen(request):
    return render(request, 'splash.html')

def main_page(request):
    if request.method == 'POST':
        # Retrieve data from AJAX Call
        decodedText = request.POST.get('decodedText')

        # Validation of QR data: To check if user scanned the correct QR code
        substring = "NUS"

        if substring not in decodedText:
            # Trigger a pop up screen?
            print("This is a test")
            messages.info(request, "Wrong QR!")  # add a welcome message
            return redirect(reverse('main_page'))

        decodedTextList = []
        
        # Test purposes
        print(request.COOKIES) 

        # Check if decodedTextList is in the cookies on client's browser
        if 'decodedTextList' in request.COOKIES:
            # Deserialise cookie into list form
            decodedTextList = json.loads(request.COOKIES['decodedTextList'])
       
        # Check if there is a repeated QRCode (List should not have any similar values)
        if decodedText not in decodedTextList:
            # Append QR data into list 
            decodedTextList.append(decodedText)

        # Test purposes
        print(decodedTextList) 
        response = JsonResponse({'success': True})

        # Set cookie
        response.set_cookie('decodedTextList', json.dumps(decodedTextList))
        return response

    return render(request, 'index.html')

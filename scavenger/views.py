import json

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Location

def splash_screen(request):
    return render(request, 'splash.html')

def main_page(request):
    locationNameList = Location.objects.values_list('location_name', flat=True).distinct()
    return render(request, 'index.html', {'locationNameList' : locationNameList})

def scan_qr_validation(request):
    if request.method == 'POST':
        # Retrieve QR Code data (i.e. location name) from AJAX Call where the data is stored in key "decodedText"
        scannedLocation = request.POST.get('decodedText')

        # Validation of QR Code data: To check if user scanned the QR Code that is generated only by our web-app
        customQRIdentifier = "NUSSOCSH23"

        # Generate error pop-up message for invalid QR Code
        if customQRIdentifier not in scannedLocation:
            print("Invalid QR! Only scan QR Codes generated by NUS SoC Scavenger Hunt Web App!")
            return JsonResponse({'success':False, 'errorMsg': 'INVALID'})
        
        # remove the customQRIdentifier from QR Code data
        scannedLocation = scannedLocation.replace(customQRIdentifier, '')

        # Create a new list "scannedLocationList" which constantly gets updated with newly scanned locations, and set it into the cookie "scannedLocationListCookie"
        scannedLocationList = []

        # Check if "scannedLocationListCookie" is in the cookies on client's browser & populate the list "scannedLocationList"
        if 'scannedLocationListCookie' in request.COOKIES:
            # Deserialise cookie into list form
            scannedLocationList = json.loads(request.COOKIES['scannedLocationListCookie'])

        # Check if there is a repeated QR Code & display warning message accordingly
        if scannedLocation in scannedLocationList:
            print(f"QR Code for this location, {scannedLocation}, already scanned! Please scan other locations!")
            return JsonResponse({'success':False, 'errorMsg': 'EXIST', 'locationName': scannedLocation})
        
        # No repeated QR Code, append the newly scanned QR Code data into list
        scannedLocationList.append(scannedLocation)
        print(f"You have found a new location - {scannedLocation}!")
        print(scannedLocationList)

        # Set the json data for success alert message
        response = JsonResponse({'success': True, 'locationName': scannedLocation})

        # Set cookie "scannedLocationListCookie"
        response.set_cookie('scannedLocationListCookie', json.dumps(scannedLocationList))

        # Check if user has completed the Scavenger Hunt game, if true set cookie "completedStatusCookie" to "yes"
        totalNoLocations = Location.objects.all().count()
        if len(scannedLocationList) == totalNoLocations:
            print("User has successfully completed NUS Soc Scavenger Hunt game 2023!")
            response.set_cookie('completedStatusCookie', 'yes')
        else:
            # User has not yet complete the game, set "completedStatusCookie" to "no"
            response.set_cookie('completedStatusCookie', 'no')
        
        # return response to AJAX call in onScanSuccess() in index.html
        return response

    return render(request, 'index.html')

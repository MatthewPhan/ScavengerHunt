import json

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Location, Event

def splash_screen(request):
    return render(request, 'splash.html')

def main_page(request):
    # Get location name and description and store it into a list. The corresponding name and description are separated by tuples. 
    locationDetailsList = Location.objects.values_list('location_name', 'location_description', 'location_image').distinct()
    # Get event name and datetime
    eventList = Event.objects.values_list('name', 'when').distinct()
    # print({'locationDetailsList': locationDetailsList, 'eventList': eventList})

    return render(request, 'index.html', {'locationDetailsList': locationDetailsList, 'eventList': eventList})

def instructions_page(request):
    # Get event name and datetime
    eventList = Event.objects.values_list('name', 'when').distinct()
    return render(request, 'instructions.html', {'eventList': eventList})

def socmaps_page(request):
    # Get event name and datetime
    eventList = Event.objects.values_list('name', 'when').distinct()
    return render(request, 'socmaps.html', {'eventList': eventList})

def acknowledgement(request):
    # Get event name and datetime
    eventList = Event.objects.values_list('name', 'when').distinct()
    return render(request, 'acknowledgement.html', {'eventList': eventList})

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

        # Create a new list of dict (location_name:location_badge) "scannedLocationList" which constantly gets updated with newly scanned locations, and set it into the cookie "scannedLocationListCookie"
        scannedLocationList = []

        # Check if "scannedLocationListCookie" is in the cookies on client's browser & populate the list "scannedLocationList"
        if 'scannedLocationListCookie' in request.COOKIES:
            # Deserialise cookie into list form
            scannedLocationList = json.loads(request.COOKIES['scannedLocationListCookie'])

        # Check if there is a repeated QR Code & display warning message accordingly
        if any(scannedLocation in loc for loc in scannedLocationList):
            print(f"QR Code for this location, {scannedLocation}, already scanned! Please scan other locations!")
            return JsonResponse({'success':False, 'errorMsg': 'EXIST', 'locationName': scannedLocation})

        # Retrieve database of corresponding location badge and fact based on the location name
        successDetails = Location.objects.get(location_name=scannedLocation)
        location_badge = str(successDetails.location_badge)
        location_fun_fact = successDetails.location_fun_fact

        # No repeated QR Code, append the newly scanned location name and badge into list
        loc_name_badge_dict = {scannedLocation : location_badge}
        scannedLocationList.append(loc_name_badge_dict)
        print(f"You have found a new location - {scannedLocation}!")
        print(scannedLocationList)

        # Set the json data for success alert message
        response = JsonResponse({'success': True, 'locationName': scannedLocation, 'locationFact': location_fun_fact, 'locationBadge': location_badge})

        # Set cookie "scannedLocationListCookie"
        response.set_cookie('scannedLocationListCookie', json.dumps(scannedLocationList), max_age=86400)

        # Check if user has completed the Scavenger Hunt game, if true set cookie "completedStatusCookie" to "yes"
        totalNoLocations = Location.objects.all().count()
        if len(scannedLocationList) == totalNoLocations:
            print("User has successfully completed NUS Soc Scavenger Hunt game 2023!")
            response.set_cookie('completedStatusCookie', 'yes', max_age=86400)
        else:
            # User has not yet complete the game, set "completedStatusCookie" to "no"
            response.set_cookie('completedStatusCookie', 'no', max_age=86400)
        
        # return response to AJAX call in onScanSuccess() in index.html
        return response

    return render(request, 'index.html')

def scan_redeem_check(request):
    if request.method == 'POST':
        # Retrieve QR Code data (i.e. location name) from AJAX Call where the data is stored in key "decodedText"
        scannedQr = request.POST.get('decodedText')

        # Validation of QR Code data: To check if user scanned the QR Code that is generated only by our web-app
        customRedeemIdentifier = "REDEEMSMOOYVOUCHERNUS"

        # Check if prizeRedeemedCookie exists, and set to "no" if does not exist 
        if 'prizeRedeemedCookie' not in request.COOKIES:
            response = JsonResponse({'success': False})
            response.set_cookie('prizeRedeemedCookie', 'no', max_age=86400)

        # Generate error pop-up message for invalid QR Code
        if customRedeemIdentifier not in scannedQr:
            print("Invalid QR! Please scan the Redeem Prize QR from Student Ambassador!")
            return JsonResponse({'success':False, 'errorMsg': 'INVALID'})

        # Set cookie "prizeRedeemedCookie" to "yes" since it passed the check
        response = JsonResponse({'success': True})
        print("User successfully redeemed the prize!")
        response.set_cookie('prizeRedeemedCookie', 'yes', max_age=86400)
        
        # return response to AJAX call in onScanSuccessRedeem()
        return response

    return render(request, 'index.html')

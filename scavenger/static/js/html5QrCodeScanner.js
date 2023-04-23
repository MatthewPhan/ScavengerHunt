// HTML5QrcodeScanner
const html5QrcodeScanner = new Html5QrcodeScanner(
"qr-reader", { fps: 10, qrbox: 250, rememberLastUsedCamera: false });

// Process QR Code using HTML5QRcodeScanner
function onScanSuccess(decodedText, decodedResult) {
    
    // Close the QR code scanning after the result is retrieved, do so by using javascript to trigger/click the "Stop Scanning" btn
    $("#html5-qrcode-button-camera-stop").trigger("click");

    // Close the QR Scanner modal-pop automatically
    $('#qrScannerModal').modal('hide');

    // Handle on success condition with the decoded text or result
    console.log(`Scan result: ${decodedText}`, decodedResult);   

    // Send the data to the Django view using AJAX POST
    const csrfToken = $('[name="csrfmiddlewaretoken"]').attr('value');

    // // Send the data to the Django view using AJAX POST
    $.ajax({
        type: 'POST',
        url: "/scan_qr_validation/",
        dataType: 'json',
        headers: {
            "X-CSRFToken": csrfToken
        },
        data: {
            'decodedText': decodedText
        },
        success: function (response, status, xhr) {
            const result = response['success'];
            if (result) {

                // Display success alert
                const newLocation = response['locationName'];
                console.log("You have found a new location - " + newLocation + "!");
                Swal.fire({
                    title: "Good job!",
                    text: "You have found a new location - " + newLocation + "!",
                    icon: 'success'
                })

                // Change the CSS of the newly scanned location by adding the custom CSS class "neon-green" 
                document.getElementById(newLocation).classList.add("neon-green");

                // Run completedStatus() to determine if user has completed the game after this scan
                completedStatus();

            }
            else {
                const errMsg = response['errorMsg'];

                // Display invalid QR Code alert
                if (errMsg === "INVALID") {
                    console.log("Invalid QR! Only scan QR Codes generated by NUS SoC Scavenger Hunt Web App!");
                    Swal.fire({
                        title: "Oops!",
                        text: "Invalid QR! Only scan QR Codes generated by NUS SoC Scavenger Hunt Web App!",
                        icon: 'error'
                    })
                }

                // Display duplicate QR Code alert
                if (errMsg === "EXIST") {
                    const location = response['locationName'];
                    console.log("QR Code for this location, '" + location + "' already scanned! Please scan other locations!");
                    Swal.fire({
                        title: "Already Scanned!",
                        text: "QR Code for this location, '" + location + "' already scanned! Please scan other locations!",
                        icon: 'warning'
                    })
                }
            }
        },
        // a failure callback that gets invoked in case there is any error while making the request
        error: function (xhr, status, error) {
            console.log(xhr.responseText);
        }
    });

}

// Style all the icons in cookie "scannedLocationListCookie" (to run this everytime web app loads)
function scannedLocationsStyle(){
    // Get the value of cookie "scannedLocationListCookie", note it returns a string representation, [\"location_1\"\054 \"location_2\"..]
    let scannedLocationListCookieValue = Cookies.get('scannedLocationListCookie');
    
    // Only process accordingly when there are values in the cookie "scannedLocationListCookie"
    if (scannedLocationListCookieValue) {
        // Convert the string representation to list
        scannedLocationListCookieValue = JSON.parse(scannedLocationListCookieValue.replaceAll("\\054", ",").replaceAll("\\", ""));
        console.log(scannedLocationListCookieValue);
        
        // Change the CSS for all the locations that are already scanned (loop through the list) by adding the custom CSS class "neon-green"
        for (let i = 0; i < scannedLocationListCookieValue.length; i++) {
            document.getElementById(scannedLocationListCookieValue[i]).classList.add("neon-green");
        }
    }
}

// Determine if user completed the game by checking cookie "completedStatusCookie" & style the web app accordingly (to run this everytime web app loads)
function completedStatus(){
    // Get the value of cookie "completedStatusCookie"
    let completedStatusCookieValue = Cookies.get('completedStatusCookie');
    if (completedStatusCookieValue === 'yes') {
        // Show the hidden django-social-share modal pop-up
        console.log("User has successfully completed NUS Soc Scavenger Hunt game 2023!");
        $('#socialShareModal').modal('show');
    }
}

// Close the scanner
function closeScannerModal(){
    // Stop the scan
    $("#html5-qrcode-button-camera-stop").trigger("click");
}

// Remove the original styling and added custom CSS Styling
document.querySelector('#qr-reader').removeAttribute('style');

// Render the QR Scanner
html5QrcodeScanner.render(onScanSuccess);
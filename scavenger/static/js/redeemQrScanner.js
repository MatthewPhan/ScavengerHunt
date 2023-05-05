// HTML5QrcodeScanner (might throw an error msg for instructions.html & socmaps.html as the id "qr-reader" only exists in index.html - small matter)
const redeemHtml5QrcodeScanner = new Html5QrcodeScanner(
    "redeem-qr-reader", { fps: 10, qrbox: 250, rememberLastUsedCamera: false });

// Process QR Code using HTML5QRcodeScanner
function onScanSuccessRedeem(decodedText, decodedResult) {

    // Close the QR code scanning after the result is retrieved, do so by using javascript to trigger/click the "Stop Scanning" btn
    $("#html5-qrcode-button-camera-stop").trigger("click");

    // // Close the QR Scanner modal-pop automatically
    $('#qrScannerModalRedeem').modal('hide');

    // Handle on success condition with the decoded text or result
    console.log(`Scan result: ${decodedText}`, decodedResult);

    // Send the data to the Django view using AJAX POST
    const csrfTokenRedeem = $('[name="csrfmiddlewaretoken"]').attr('value');

    // // Send the data to the Django view using AJAX POST
    $.ajax({
        type: 'POST',
        url: "/scan_redeem_check/",
        dataType: 'json',
        headers: {
            "X-CSRFToken": csrfTokenRedeem
        },
        data: {
            'decodedText': decodedText
        },
        success: function (response, status, xhr) {
            const result = response['success'];
            if (result) {

                // Display "Smooy Voucher Redeemed!" & disable the btn "Redeem Prize"
                console.log("User has successfully redeemed the Smooy Voucher!");
                const img = document.createElement("img");
                img.src = "/media/badges/redeemed-removebg.png";
                const src = document.getElementById("redeemStatus");
                src.appendChild(img);
                document.getElementById("redeembtn").style.display= 'none';

                // reload browser to prevent the possibility of HTML5QrScanner bug of infinite ajax calls
                window.location.reload();
            }
            else {
                // User scanned invalid QR, 
                const errMsg = response['errorMsg'];

                // Display invalid QR Code alert
                if (errMsg === "INVALID") {
                    console.log("Invalid QR! Please scan the Redeem Prize QR from Student Ambassador!");
                    Swal.fire({
                        title: "Oops!",
                        text: "Invalid QR! Please scan the Redeem Prize QR from Student Ambassador!",
                        icon: 'error'
                    })
                    // reload browser to prevent the possibility of HTML5QrScanner bug of infinite ajax calls, give a 1.5 seconds time of displaying the invalid modal pop-up
                    setTimeout(function(){
                        window.location.reload();
                     }, 1500);
                }
            }
        },
        // a failure callback that gets invoked in case there is any error while making the request
        error: function (xhr, status, error) {
            console.log(xhr.responseText);
        }
    });

}

// Close the scanner
function closeRedeemScannerModal() {
    // Stop the scan
    $("#html5-qrcode-button-camera-stop").trigger("click");

    // Close this modal, set the modal to display none
    document.getElementById("qrScannerModalRedeem").style.display = "none";

}

// Determine if user already redeemed the prize the game by checking cookie "prizeRedeemedCookie" & style the web app accordingly (to run this everytime web app loads)
function redeemStatusCheck() {
    // Get the value of cookie "prizeRedeemedCookie"
    let prizeRedeemedCookieValue = Cookies.get('prizeRedeemedCookie');
    if (prizeRedeemedCookieValue === 'yes') {
        // Show the hidden django-social-share modal pop-up
        console.log("User has already redeemed the prize!");
        const img = document.createElement("img");
        img.src = "/media/badges/redeemed-removebg.png";
        const src = document.getElementById("redeemStatus");
        src.appendChild(img);
        document.getElementById("redeembtn").style.display= 'none';
    }
}

// Remove the original styling and added custom CSS Styling
document.querySelector('#redeem-qr-reader').removeAttribute('style');

// Render the QR Scanner
redeemHtml5QrcodeScanner.render(onScanSuccessRedeem);
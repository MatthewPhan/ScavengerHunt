# NUS SoC Scavenger Hunt Game Web App

## Background
A mobile web application that allows users to participate in a scavenger hunt game using their mobile devices to scan custom QR Codes generated through our admin dashboard. This mobile web app is built on the Django framework with a lightweight [Html5-QRCode library](https://github.com/mebjas/html5-qrcode).

## Developers
- [James Teo](https://github.com/twhjames)
- [Matthew Phan](https://github.com/MatthewPhan)

## Developer Guide

### Development Environment Background
For our development server, we are running Ubuntu Server 20.04 LTS on AWS EC2 (free tier). Note that this web app requires direct access to the camera, which is a powerful feature, as such it requires consent from the user, and the site MUST be on a secure origin (HTTPS). Our development server, it contains a locally trusted SSL certificate, generated through [mkcert](https://github.com/FiloSottile/mkcert) \(ideally for production deployment, you should generate an SSL certificate using [Let's Encrypt](https://www.penta-code.com/how-to-get-free-https-in-10-minutes-with-letsencrypt-and-certbot/), a free and open certificate authority\).

### Installation
1. Install pip, if haven’t  
   `sudo apt install python3-pip -y`
2. Install Django, if haven’t  
   `sudo apt install python3-django`
3. Pip Install the relevant packages for the web app as such  
   `sudo python3 -m pip install djangorestframework django-cors-headers django-sslserver qrcode Pillow django-jquery django-cleanup`
4. To run the program on localhost, enter the following command  
   `sudo python3 manage.py runsslserver 0.0.0.0:8000 --certificate cert.pem --key key.pem`
5. Do note that we have imported the following third-party API libraries as well \(no action required\): 
   - [sweetalert2](https://sweetalert2.github.io/)
   - [js-cookie](https://github.com/js-cookie/js-cookie/tree/latest#readme)
   - [jquery](https://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js)
   - [html5-qrcode](https://github.com/mebjas/html5-qrcode)

## Admin Guide
### Django Admin Generate Custom QR Code
1. Login into the Django Admin Dashboard https://<domain_url>/admin.
2. Click on the link “add” under Locations model.
3. Enter the location name and hit the “save” button.
4. The new custom QR code for the location can be found in the following directory on the **server**: *Scavengerhunt/media/qrcodes*

## User Guide
- Unscanned locations are styled with neon-white color.  
- Scanned locations will be styled in neon-green color.  
- To scan QR Codes, the user can:  
   - Scan via camera (choose front or back camera), or  
   - Import image (in the event their browser is incompatible with webcam access, or that both their front and back cameras are spoilt..)  
- Upon successful completion of the event, they can share a custom congratulatory image or text with a link, depending on which mobile phone they are using (due to Webshare API Browser Compatibility):  
   - Instagram (image for stories, feed & chat)
   - Twitter (image for DM & Tweet)
   - Facebook (image for both Facebook & story)


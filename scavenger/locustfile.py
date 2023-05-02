import time
from locust import HttpUser, task, between

class WebsiteUserTest(HttpUser):
    wait_time = between(1, 5)

    # Index.html get request 
    @task
    def index_page(self):
       self.client.get('/index/', verify=False)

    # Ajax post call request header
    @task
    def create_post(self):

        header = {
            'Host': '127.0.0.1:8000',
            'Connection': 'keep-alive',
            'Content-Length': '31',
            'accept': 'application/json',
            'Origin': 'https://127.0.0.1:8000',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://127.0.0.1:8000/index/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',

            # To be changed accordingly
            'X-CSRFToken': 'eYSM8s0T6bLk1E6lIilFTaaDrY6lNaNldcFhXqdYO3mI1H9NTYRyALPcUbrE21zg',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'csrftoken=9oXFZ8nfS2LyaddClQG3RLPJDnvtp1W5; sessionid=4rcmahfj536uhftqsanxt432elq9i6yp; completedStatusCookie=no; scannedLocationListCookie="[\"Fintech Lab\"\054 \"Cool Spot\"]"'
        }

        self.client.post("/scan_qr_validation/", verify=False , headers=header ,data=
        {
            "decodedText": "Fintech LabNUSSOCSH23"
        }
        )


    # HTML5QRCodeScanner API
    @task
    def testqrAPI(self):
        self.client.get(url='https://127.0.0.1:8000/static/js/html5QrCodeScanner.js', verify=False)

    @task
    def testsocialAPI(self):
        self.client.get(url="https://127.0.0.1:8000/static/js/socialShare.js", verify=False)
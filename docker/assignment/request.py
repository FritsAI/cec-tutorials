import requests

notification_service_url = "http://notifications-service:3000/api/notify"

data = {
    "notification_type": "OutOfRange", 
    "researcher": "d.landau@uu.nl",
    "measurement_id": "1234", 
    "experiment_id": "5678", 
    "cipher_data": "D5qnEHeIrTYmLwYX.hSZNb3xxQ9MtGhRP7E52yv2seWo4tUxYe28ATJVHUi0J++SFyfq5LQc0sTmiS4ILiM0/YsPHgp5fQKuRuuHLSyLA1WR9YIRS6nYrokZ68u4OLC4j26JW/QpiGmAydGKPIvV2ImD8t1NOUrejbnp/cmbMDUKO1hbXGPfD7oTvvk6JQVBAxSPVB96jDv7C4sGTmuEDZPoIpojcTBFP2xA"
}

#request_response = requests.post(url=notification_service_url, data=data)
response = requests.post(notification_service_url,json=data)

#print(request_response.text)
print(response.text)
with open('/usr/src/app/assignment/log.txt', 'a+') as file:
    # Write a string to the file
    file.write(response.text + '\n')


import requests
body = {
    'Accelerometer_x': 0.094,
    'Accelerometer_y': 0.759,
    'Accelerometer_z': 0.774,
    'Gyroscope_x': 17.585,
    'Gyroscope_y': 3.231,
    'Gyroscope_z': 1.451
    }
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
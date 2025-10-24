import requests

latitude = -6.2088
longtitude = 106.8456

url = f"https://api.aladhan.com/v1/timings?latitude={latitude}&longitude={longitude}&method=20"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    timings = data["data"]["timings"]
    date = data["data"]["date"]["readable"]


    print(f"() jadwal salat untuk tanggal {date}")
    print("" * 40)
    print(f"imsak     : {timings['imsak']}")
    print(f"subuh     : {timings['fajr']}")
    print(f"terbit    : {timings['sunrise']}")
    print(f"ashar     : {timings['asr']}")
    print(f"maghrib   : {timings['maghrib']}")
    print(f"isya      : {timings['isha']}")
    print("-" * 40)

else:
    print(f"X gagal ambil data dari API. Status code : {response.status_code}")    
    






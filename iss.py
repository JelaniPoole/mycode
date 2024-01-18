#!/usr/bin/env python3

import requests

URL= "http://api.open-notify.org/iss-now.json"

def main():
    resp= requests.get(URL).json()

    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["longitude"]

    ts= resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)

    print(f"""Current Location of the ISS:
    Timestamp: {datetime_time}
    Lon: {lon}
    Lat: {lat}""")

if __name__ == "__main__":
    main()

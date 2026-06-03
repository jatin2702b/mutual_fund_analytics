import requests
import pandas as pd

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    response = requests.get(f"https://api.mfapi.in/mf/{code}")
    data = response.json()

    df = pd.DataFrame(data["data"])
    df.to_csv(f"data/raw/{name}_live.csv", index=False)

    latest_nav = data["data"][0]
    print(f"{name} | NAV: {latest_nav['nav']} | Date: {latest_nav['date']}")

print("Live NAV fetch completed.")

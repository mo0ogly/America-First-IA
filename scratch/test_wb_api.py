import urllib.request
import json

def fetch_wb_data(country_code, indicator, year=2022):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?date={year}&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if len(data) > 1 and data[1]:
                val = data[1][0]['value']
                return val
    except Exception as e:
        print(f"Error fetching {indicator} for {country_code}: {e}")
    return None

print("Fetching R&D researchers per million for USA (2022):", fetch_wb_data("US", "SP.POP.SCIE.RD.P6"))
print("Fetching population for USA (2022):", fetch_wb_data("US", "SP.POP.TOTL"))

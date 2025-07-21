import requests

def get_industry_from_clearbit(domain):
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    url = f"https://company.clearbit.com/v2/companies/find?domain={domain}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("category", {}).get("industry")
    else:
        return "Unknown"

import requests


def convertADtoBS(year, month, day):
    try:
       
        year = int(year)
        month = int(month)
        day = int(day)
        
        
        url = f"https://sudhang.pythonanywhere.com/ADtoBS/{year}/{month}/{day}"
      
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if "bs_date" in data:
                return data["bs_date"]
            else:
                return {"error": data.get("error", "Unknown error")}
        else:
            return {"error": f"Unable to connect to API, status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def convertBStoAD(year, month, day):
    try:
        
        year = int(year)
        month = int(month)
        day = int(day)
        
        
        url = f"https://sudhang.pythonanywhere.com/BStoAD/{year}/{month}/{day}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if "ad_date" in data:
                return data["ad_date"]
            else:
                return {"error": data.get("error", "Unknown error")}
        else:
            return {"error": f"Unable to connect to API, status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

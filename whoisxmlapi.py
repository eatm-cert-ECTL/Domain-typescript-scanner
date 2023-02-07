from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlretrieve
from flashScreenshot import SCREENSHOTS_FOLDER
import json
import requests
import datetime
import urllib

SCREENSHOTS_FOLDER = "screenshots"

def reverseWhois_request(keyword: str, dateFrom: datetime.datetime,dateTo: datetime.datetime) -> list:
    """Send a reversewhois request to Whoisxmlapi for the given keyword after the given date.

    Args:
        keyword (str): Keyword to look for
        dateFrom (datetime.datetime): Date after which we want the created domains

    Raises:
        reverseWhoisException: Raised when the request doesn't succed

    Returns:
        list: List of generated domains.
    """
    
    with open("API_Keys/WhoisXml_key") as f:
        WHOISXML_KEY = f.read()
    url = "https://reverse-whois.whoisxmlapi.com/api/v2"
    body = {
            "apiKey": WHOISXML_KEY,
            "searchType": "current",
            "mode": "purchase",
            "punycode": True,
            "createdDateFrom": dateFrom.strftime("%Y-%m-%d"),
            "createdDateTo": dateTo.strftime("%Y-%m-%d"),
            "advancedSearchTerms": [{
                "field": "DomainName",
                "term": "",
                "exclude": False
            }]
        }
    body["advancedSearchTerms"][0]["term"] = f"*{keyword}*"
    response = requests.post(url,data=json.dumps(body),headers={'Content-type': 'application/json'})
    if response.status_code == 200:
        return response.json()["domainsList"]
    else:
        print(f"Whoisxmlapi error during reverse whois request: {response.reason}")
        raise ReverseWhoisException(f"Whoisxmlapi error during reverse whois request: {response.reason}")

class ReverseWhoisException(Exception):
    pass

class Whois_Analysis:
    def __init__(self,domain: str) -> None:
        self.domain = domain
        self.response = None

    def whois_request(self):
        with open("API_Keys/WhoisXml_key") as f:
            WHOISXML_KEY = f.read()
        url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={WHOISXML_KEY}&domainName={self.domain}&outputFormat=JSON&preferFresh=1"
        response = requests.get(url)
        if response.status_code == 200:
            self.response = response.json()["WhoisRecord"]
        else:
            self.response = {}
            raise WhoisException(f"Whoisxmlapi error during whois request: {response.reason}")

class WhoisException(Exception):
    pass

def screenshot_request(domain:str,folder:str=SCREENSHOTS_FOLDER) -> Path:
    with open("API_Keys/WhoisXml_key") as f:
            WHOISXML_KEY = f.read()
    location = Path(folder,str(domain) + ".jpg")
    params = urlencode(dict(apiKey=WHOISXML_KEY,url=f"http://{domain}",credits="DRS",mode="slow"))

    i = 0
    while i < 3:
        try:
            print(urlretrieve("https://website-screenshot.whoisxmlapi.com/api/v1?" + params, location))
            return Path(str(location))
        except urllib.error.HTTPError as e:
            print(f"{domain} Taking screenshot error with whoisxmlapi API : {str(e)}")
            print("Retry...")
        finally:
            i += 1
    print("All tries failed...")
    return Path("")


if __name__ == "__main__":
    output = reverseWhois_request("airways",datetime.datetime(2021,8,23))
    #print(screenshot_request("airfrance.com"))
    print(output)
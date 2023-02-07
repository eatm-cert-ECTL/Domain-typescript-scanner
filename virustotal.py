import requests
import socket
import json

class Virustotal_Analysis:

    def __init__(self,domain:str) -> None:
        """Object getting virustotal analysis from a domain name

        Args:
            domain (:class:`str`): Domain name to analyse.
        """
        self.domain = domain
        self.nbrPositive = ""
        self.response = None

    def virustotal_request(self) -> None:
        """Get the virustotal request for the chosen domain using the API Key

        Returns:
            bool: True if the request is succesful, False otherwise.
        """
        with open("API_Keys/virustotal_key") as f:
            VIRUSTOTAL_KEY = f.read()
        url = "https://www.virustotal.com/api/v3/domains/{}".format(self.domain)
        header = {'x-apikey': VIRUSTOTAL_KEY}
        response = requests.get(url,headers=header)
        if response.status_code != 200:
            print('GET /tasks/ {}'.format(response.status_code))
            self.response = {}
            return False
        else:
            self.response = response.json()['data']
            #TODO test with non analysed domains
            self.nbrPositive = self.response['attributes']['last_analysis_stats']['malicious'] + self.response['attributes']['last_analysis_stats']['suspicious']
            return True

def virustotal_resolution(domain: str) -> list[str]:
    with open("API_Keys/virustotal_key") as f:
            VIRUSTOTAL_KEY = f.read()
    ip = socket.gethostbyname(domain)
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}/resolutions?limit=40".format(ip)
    header = {'x-apikey': VIRUSTOTAL_KEY}
    domains = []
    response = requests.get(url,headers=header)
    if response.status_code == 200:
        response = response.json()
        for elt in response['data']:
            d = elt["attributes"]["host_name"]
            if not d.startswith("www"):
                domains.append(d)
        #url = response["links"]["next"]
    else:
        msg = f"Virustotal Resolution error: {response.reason}"
        print(msg)
        print(json.dumps(response.json(),indent=4))
        raise VirustotalResolutionException(msg)
    #print(f"domains : {domains}\n len : {len(domains)}")
    return domains

class VirustotalResolutionException(Exception):
    pass

if __name__ == "__main__":
    virustotal_resolution("delta-airlineus.com")
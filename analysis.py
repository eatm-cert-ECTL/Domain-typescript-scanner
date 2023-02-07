import requests
from requests.models import HTTPError, Response


def get_request(url : str) -> Response:
    """Get response form GET request

    Args:
        url (:class:`str`): Requested url

    Raises:
        HTTPError: Error raised if the status code is different from 200 (200 = succes)

    Returns:
        :class:`Response`: Request response
    """
    resp = requests.get(url)
    if resp.status_code != 200:
        print('GET /tasks/ {}'.format(resp.status_code))
        raise HTTPError
    return resp



class IPQS_Analysis:

    def __init__(self,domain : str) -> None:
        """Object managing IPQS analysis

        Args:
            domain (:class:`str`): domain name to be analysed
        """
        self.domain = domain
        self.score = None
        self.unsafe = None
        self.ip_adress = None
        self.parking = None
        self.spamming = None
        self.malware = None
        self.phishing = None
        self.suspicious = None
        self.adult = None
        self.response = None


    def IPQS_request(self) -> None:
        """Send request for the chosen domain using API Key
        """
        with open("API_Keys/IPQS_key") as f:
            IPQS_KEY = f.read()
        try:
            self.response = get_request("https://ipqualityscore.com/api/json/url/{}/{}".format(IPQS_KEY,self.domain)).json()
            #for todo_item in self.response:
            #        print("{}: {}".format(todo_item,self.response[todo_item]))
            if self.response['success']:
                self.score = self.response['risk_score']
                self.unsafe = self.response['unsafe']
                try:
                    self.ip_address = self.response['ip_address']
                except KeyError as e:
                    print(e)
                self.parking = self.response['parking']
                self.spamming = self.response['spamming']
                self.malware = self.response['malware']
                self.phishing = self.response['phishing']
                self.suspicious = self.response['suspicious']
                self.adult = self.response['adult']

        except HTTPError as e:
            print(e)

    def get_complete_response(self) -> str:
        return str(self.response)
import requests
import re



class WaybackAnalysis:

    def __init__(self, domain:str) -> None:
        self.domain = domain

        self.wayback_url = "https://web.archive.org/web/*/http://" + domain

        url = "http://" + domain
        wburl = "http://web.archive.org/web/timemap/link/http://" + url

        response = requests.get(wburl,verify=False)

        self.response = response.content.decode().split('\n')

        length = len(self.response)
        
        self.number_archives = 0
        self.first_date = ""
        self.last_date = ""

        if length >= 4:
            self.number_archives = length - 4
            reg_expr = "datetime=\"(.*)\""

            first = re.search(reg_expr, self.response[3])
            if first:
                self.first_date = first.group(1)

            last = re.search(reg_expr, self.response[-2])
            if last:
                self.last_date = last.group(1)


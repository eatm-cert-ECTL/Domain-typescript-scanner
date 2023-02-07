import os
from pathlib import Path

import whoisxmlapi
from whoisxmlapi import WhoisException, Whois_Analysis
import threaded_job_queue
import virustotal
import analysis
from wayback_machine_request import WaybackAnalysis

from PyQt5.QtCore import QThread, pyqtSignal


domain_dict = {}

class FullAnalysis:
    def __init__(self, domain:str,doIPQS:bool=True,doVirustotal:bool=True,doScreenshot:bool=True) -> None:
        """Represents the analysis of a domain

        Args:
            domain (:class:`str`): The domain to analyse
            doIPQS (bool, optional): Do IPQS ?. Defaults to True.
            doVirustotal (bool, optional): Do Virustotal ?. Defaults to True.
        """
        self.domain = domain
        self.whois_analysis = Whois_Analysis(domain)
        try:
            self.whois_analysis.whois_request()
        except WhoisException as e:
            print(str(e))
        self.ipqs = analysis.IPQS_Analysis(domain)
        if doIPQS:
            self.ipqs.IPQS_request()
        self.virustotal_analysis = virustotal.Virustotal_Analysis(domain)
        if doVirustotal:
            self.virustotal_analysis.virustotal_request()
        self.waybackAnalysis = WaybackAnalysis(domain)
        self.imagePath = Path("")
        if doScreenshot:
            self.imagePath = whoisxmlapi.screenshot_request(domain)
        


def exec_function(domain:str,doIPQS:bool=True,doVirustotal:bool=True,doScreenshot:bool=True) -> None:
    """Function to execute by the job queue

    Args:
        domain (:class:`str`): the domain to analyse
        doIPQS (bool, optional): Do IPQS ?. Defaults to True.
        doVirustotal (bool, optional): Do Virustotal ?. Defaults to True.
    """
    domain_dict[domain]=FullAnalysis(domain,doIPQS=doIPQS,doVirustotal=doVirustotal,doScreenshot=doScreenshot)



class Worker(QThread):
    finished = pyqtSignal()
    output = pyqtSignal(dict)
    advancement = pyqtSignal(int)
    
    def __init__(self, domains:list[str]) -> None:
        """A worker that runs on a separate thread from the main application, that launches the analysis of all given domains

        Args:
            domains (:class:`str`): the domain to analyse
        """
        super().__init__()
        self.domains = domains
    
    
    def run(self) -> None:
        """Run the worker
        """
        
        q = threaded_job_queue.Job_Queue(lambda x: exec_function(x,doIPQS=os.path.isfile("API_Keys/IPQS_key"),doVirustotal=os.path.isfile("API_Keys/virustotal_key"),doScreenshot=os.path.isfile("API_Keys/WhoisXml_key")), self.domains)
        q.advancement.connect(lambda x: self.advancement.emit(x))
        
        
        #if not os.path.isfile("API_Keys/IPQS_key"):
        #    QMessageBox.critical(None, "API_Key Error","No IPQS key found")
        #if not os.path.isfile("API_Keys/virustotal_key"):
        #    QMessageBox.critical(None, "API_Key Error","No Virustotal key found")
        q.run_job_queue()

        self.output.emit(domain_dict)

        self.advancement.emit(100)
        self.finished.emit()
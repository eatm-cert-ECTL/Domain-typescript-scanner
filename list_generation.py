import os
import re
import sys
import datetime
import whoisxmlapi
from whoisxmlapi import reverseWhois_request
import importlib
from pathlib import Path

from virustotal import VirustotalResolutionException, virustotal_resolution
import database
import socket

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

class Worker(QThread):
    finished = pyqtSignal()
    errorSignal = pyqtSignal(str,str)
    
    def __init__(self, parent, base_domain_name:str, use_dnstwist:bool, use_different_tld:bool, use_urlcrazy:bool,use_reverse_whois:bool,use_virustotal:bool) -> None:
        super().__init__()
        self.parent = parent
        self.model = parent.model
        self.base_domain_name = base_domain_name
        self.use_dnstwist = use_dnstwist
        self.use_different_tld = use_different_tld
        self.use_urlcrazy = use_urlcrazy
        self.use_reverse_whois = use_reverse_whois
        self.use_virustotal = use_virustotal
    
    
    def run(self) -> None:
        output = []
        domainsWithoutIP = []

        if self.use_reverse_whois:
            try:
                keywords = []
                beginQdate = self.parent.reverseWhoisCalendar.selectedDate()
                beginDate = datetime.datetime(beginQdate.year(),beginQdate.month(),beginQdate.day())
                endQdate = self.parent.endCalendarWidget.selectedDate()
                endDate = datetime.datetime(endQdate.year(),endQdate.month(),endQdate.day())
                with open(self.parent.keywordsListSelectorWidget.path) as f:
                    keywords += f.readlines()
                for keyword in keywords:
                    doms = reverseWhois_request(keyword,beginDate,endDate)
                    output += doms
                    if self.use_virustotal:
                        for domain in doms:
                            try:
                                output += virustotal_resolution(domain)
                            except socket.gaierror as e:
                                print(e.errno)
                                if e.errno == -5 or e.errno == -3:
                                    domainsWithoutIP.append(domain)
                    database.insertIntoDatabase2([keyword],self.parent.databaseName,self.parent.keywordsTableName)
                    self.parent.keywordsModel.select()
                if domainsWithoutIP != []:
                    self.errorSignal.emit("Virustotal Resolution Error",f"All these domains have no IP adresses but have a whois records updated or created in the time period : {domainsWithoutIP}")
            except whoisxmlapi.ReverseWhoisException as e:
                self.errorSignal.emit("Reverse Whois Error",str(e))
            except VirustotalResolutionException as e:
                self.errorSignal.emit("Virustotal Resolution Error",str(e))
            except Exception as e:
                print(e)
                self.errorSignal.emit("Error","Reverse Whois unknown error")
        else:
            for domain in self.base_domain_name:
                output += generate_list(domain, self.use_dnstwist, self.use_different_tld, self.use_urlcrazy)
                output += generateFromUserFunctions(domain,self.parent.userFunctionsSelectorWidget.path)
            database.insertIntoDatabase2(self.base_domain_name,self.parent.databaseName,self.parent.domainsTableName)
            self.parent.domainsModel.select()
        
        
        if len(output) != 0:
            database.insertIntoDatabase(list(set(output)), self.parent)
        else:
            self.errorSignal.emit("No domain generated","No domain generated")
        self.finished.emit()


def generateFromUserFunctions(domain,userFunctionsPath:Path) -> list[str]:
    if userFunctionsPath == "":
        return []
    p = Path(userFunctionsPath)
    folderPath = p.parent
    filename = p.stem
    sys.path.append(folderPath)
    try:
        module = importlib.import_module(filename)
        try:
            output = module.generate(domain)
        except AttributeError as e:
            print(e)
            output = []
            #TODO Check if good thread
            QMessageBox.critical(None, "Generation Error", "Check if your python file has an unique function named generate which takes as paremeter a string corresponding to the domain name and return the generated domains as a list of string")
    except SyntaxError as e:
        print(e)
        QMessageBox.critical(None,"User lib load error", "The provided file is not a valid python file")
        output = []
    return output


def dnstwist_generation(base_domain_name:str, use_different_tld:bool) -> list[str]:
    stream = os.popen("./libs/dnstwist.py --format list " + base_domain_name)
    output = stream.read()
    domain_list = output.split('\n')
    domain_list = domain_list[:len(domain_list)-1]
    if use_different_tld:
        tlds = ['com','net','eu','cn','ga','gq','tk','ml','cf','cc','info','app','ooo','xyz','online','site','wang','work','rest','buzz','top','fit']
        domain_list2 = []
        for elem in domain_list:
            #get the domain name without the tld
            i = elem.rfind(".")
            domain = elem[0:i+1]
            for tld in tlds:
                domain_list2.append(domain + tld)
        domain_list += domain_list2
    return domain_list



def urlcrazy_generation(base_domain_name:str) -> list[str]:
    stream = os.popen("./libs/urlcrazy/urlcrazy -r -i " + base_domain_name)
    output = stream.read()
    output_list = output.split('\n')
    domain_list = []
    for elem in output_list[11:len(output_list)-3]:
        #remove coloration characters here since --nocolor option on urlcrazy does not work
        elem = elem.replace("\x1b[1;39;49m", '')
        elem = elem.replace("\x1b[0m", '')
        domain_list.append((re.split(' +', elem))[-3])
    return domain_list



def generate_list(base_domain_name:str, use_dnstwist:bool, use_different_tld:bool, use_urlcrazy:bool) -> list[str]:
    domain_list = [base_domain_name]
    if use_dnstwist:
        domain_list += dnstwist_generation(base_domain_name, use_different_tld)
    if use_urlcrazy:
        domain_list += urlcrazy_generation(base_domain_name)
    return domain_list
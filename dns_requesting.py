import sqlite3
import PyQt5

from dns.resolver import NoAnswer
import threaded_job_queue

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget

try:
	from dns.resolver import Resolver, NXDOMAIN, NoNameservers
	import dns.rdatatype
	from dns.exception import DNSException
	MODULE_DNSPYTHON = True
except ImportError:
	MODULE_DNSPYTHON = False


existing_domains = []

def exec_function(domain : str) -> None:
    """The function to execute by the job queue
       This one makes dns requests for IPv4 and IPv6 addresses to check the existence of the given domain 
    Args:
        domain (:class:`str`): the domain for which to check existence
    """
    resolv = Resolver()

    try:
        # Check for IPv4
        resolv.resolve(domain, rdtype=dns.rdatatype.A)
        existing_domains.append(domain)
    except NXDOMAIN:
        pass
    except NoNameservers:
        print(domain + ' !ServFail')
    except NoAnswer as e:
        try:
            #Check for IPv6
            resolv.resolve(domain, rdtype=dns.rdatatype.AAAA)
            existing_domains.append(domain)
        except NoAnswer as e:
            print(domain + " " +str(e))
        except DNSException as e:
            print(domain + " " + str(e))
    except DNSException as e:
        print(domain + " " + str(e))


class Worker(QThread):
    finished = pyqtSignal()
    advancement = pyqtSignal(int)

    def __init__(self, parent : QWidget) -> None:
        """A worker that runs on a separate thread from the main application, that launches the dns requesting of all given domains and changes the database accordingly

        Args:
            parent (:class:`QWidget`): [description]
        """
        super().__init__()
        self.parent = parent
    
    def run(self) -> None:
        """Run the worker
        """
        con = sqlite3.connect(self.parent.databaseName)
        cur = con.cursor()
        request = "SELECT domains FROM {} WHERE (isWhitelisted == 0 AND isBlacklisted == 0)".format(self.parent.typosquatDomainTableName)
        
        q = threaded_job_queue.Job_Queue(exec_function, [domain[0] for domain in cur.execute(request)])
        q.advancement.connect(lambda x: self.advancement.emit(x))
        q.run_job_queue()
        
        if len(existing_domains) > 0:
            request = "UPDATE {} SET registered = 1 WHERE domains IN (".format(self.parent.typosquatDomainTableName)
            for domain in existing_domains:
                request += '"{}",'.format(domain)
            request = request[:len(request)-1] 
            request += ")"
            cur.execute(request)
            con.commit()
        con.close()

        self.parent.model.setFilter("registered==1")
        self.parent.model.select()
        self.parent.typosquatDomainsTableView.resizeColumnsToContents()

        self.advancement.emit(100)
        self.finished.emit()







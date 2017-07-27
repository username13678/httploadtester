"""
Implements an HTTP Loadtester.
"""
import httplib
import time
from collections import Counter
from Queue import Queue
from threading import Thread

class ConnectionLoadTester(Thread):
    """ Implements an HTTP Loadtester on a single HTTP connection."""
    def __init__(self, url, requests, responses):
        Thread.__init__(self)
        self.daemon = True
        self.connection = httplib.HTTPConnection(url, timeout=2)
        self.requests = requests
        self.responses = responses

    def run(self):
        """ Sends the requests in self.requests. Writes the responses status
        to self.responses."""
        while True:
            request = self.requests.get()
            latency = 0
            status = None
            try:
                begin = time.time()
                self.connection.request(*request)
                status = self.connection.getresponse().status
                latency = time.time() - begin
            finally:
                self.responses.put((status, latency))
                self.requests.task_done()

class ConnectionPool(object):
    """ Represents a pool of Connections."""
    def __init__(self, url, concurrent):
        """ Initialize the pool, its queues and starts its connections.

        self.requests contains the HTTP requests to send.
        self.responses contains the HTTP responses status of the requests.
        """
        self.requests = Queue(concurrent)
        self.responses = Queue()
        for _ in range(concurrent):
            connection_load_tester = ConnectionLoadTester(
                url, self.requests, self.responses)
            connection_load_tester.start()

    def add_request(self):
        """ Adds a request to self.requests."""
        self.requests.put(('GET', '/'))

    def finish(self):
        """ Waits for all the requests to be done and counts the reponses.

        Returns:
            The number of response status 200 we got
            The number of response status 500 we got
            The minimum latency
            The maximum latency
            The mean latency
            The number of requests sent
        """
        counter = Counter()
        latencies = []
        while not self.responses.empty():
            status, latency = self.responses.get_nowait()
            counter[status] += 1
            latencies.append(latency)
        return (counter[200],
                counter[500],
                min(latencies),
                max(latencies),
                sum(latencies)/len(latencies),
                len(latencies))



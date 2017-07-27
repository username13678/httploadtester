"""
Implements an HTTP Loadtester.
"""

class LoadTester(object):
  def __init__(self, qps, concurent, duration, url):
    self.qps = qps
    self.concurrent = concurrent
    self.duration = duration
    self.url = url

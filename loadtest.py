"""
Launches the code.
"""
import argparse
import time
from loadtester import ConnectionPool

def parse_arguments():
    """Parses the command line arguments

    Returns:
        The parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Loadtests a HTTP server.')
    parser.add_argument('qps', type=int,
                        help='number of queries per second to generate')
    parser.add_argument('concurrent', type=int,
                        help=('maximum number of concurrent queries to have',
                              'in-flight'))
    parser.add_argument('duration', type=int,
                        help='duration of the test in seconds')
    parser.add_argument('url', type=str,
                        help='url to load test with HTTP GET requests')
    return parser.parse_args()

def main(qps, concurrent, duration, url):
    """Creates the ConnectionPool, the requests and display the results."""
    pool = ConnectionPool(url, concurrent)
    begin = time.time()
    while time.time() - begin < duration:
        begin_second = time.time()
        for _ in range(qps):
            pool.add_request()
        time.sleep(max(begin_second + 1 - time.time(), 0))
    status200, status500 = pool.finish()
    print('%i requests suceeded' % status200)
    print('%i requests failed' % status500)

if __name__ == "__main__":
    args = parse_arguments()
    main(args.qps, args.concurrent, args.duration, args.url)

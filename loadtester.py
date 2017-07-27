"""
Implements an HTTP Loadtester.
"""
import argparse



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

if __name__ == "__main__":
    parse_arguments()

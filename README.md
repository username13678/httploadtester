# httploadtester

# How to use me
`loadtest <qps> <concurrent> <duration> <url>`

Where the positional arguments mean:
* *qps*: number of queries per second to generate
* *concurrent*: maximum number of concurrent queries to have in-flight
* *duration*: duration of the test in seconds
* *url*: url to load test with HTTP GET requests

At the end of the test, the following statistics should be printed:
* min, max, and average latency
* actual qps sent
* number of succeeded (HTTP 200) and failed (HTTP 500) requests

# Design

## Introduction
This document details the implementation of a HTTP Loadtester.

## Webserver
This section describres the different webserver available to test.

We will give the user the possibility to use two differents webserver.
The first one, webserver.py uses the python standards library. It creates
a new thread for each request it handles.
To launch this server, please call `python webserver.py`.

The second one, uses Flask Apps, as suggested by Google. It allows the user
to start multiple processes.
To launch this server, please call `gunicorn webserver2:app -w NUMBER` where
NUMBER is the number of processes to start.

## Load tester
This section describre the loadtester code.

### Command line interface

### Multiprocessing

## Improvements

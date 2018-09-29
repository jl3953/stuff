#!/usr/bin/python2.7

""" Script for connecting via parallel connections using iperf.

This script takes in parameters (port, minimum number of parallel connections,
maximum number of parallel connections) and runs the iperf command multiple
times with min_parallel_connections to max_parallel_connections.

For the specific commands run for this assignment, please refer to the
bottom of this script.

"""

import argparse
import subprocess
import sys


def run_iperf(parallel, port=5201, time=5):

    """ Runs the iperf command given in the instructions.

    Args:
        parallel (int): the number of parallel connections with which
            client connects to server.
        port (int): port to connect to.
        time (int): time to transmit in seconds

    Returns:
        Return code from command.

    """

    # assuming that iperf3 is in current directory
    command = ["./iperf3",
        "-c", "bouygues.testdebit.info",
        "-p", str(port),
        "-t", str(time),
        "-P", str(parallel)]

    # the command might something like this:
    # ./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 3

    rc = subprocess.call(command)
    print ("rc: [%d] for command: [%s]" % (rc, " ".join(command)))
    sys.stdout.flush()

    return rc


def main():

    parser = argparse.ArgumentParser(description="Runs iperf3 multiple times")
    parser.add_argument("--port", "-p", type=int, default=5201,
            help="port to which to connect.")
    parser.add_argument("--max_parallel", "-P", type=int, required=True,
            help="max number of parallel connections.")
    parser.add_argument("--min_parallel", "-n", type=int, default=1,
            help="min number of parallel connections.")
    args = parser.parse_args()

    for parallel_connections in range(args.min_parallel, args.max_parallel + 1):
        port = args.port
        while ( 0 != run_iperf(parallel_connections, port=port)):
            # retry on failure, assuming port connection failure.
            print ("iperf failed on port: [%d], re-trying on port: [%d]" 
                    % (port, port + 1))
            sys.stdout.flush()
            port = port + 1

    return 0;


if __name__ == "__main__":
    sys.exit(main())


""" The specific commands run for this assignment are listed below. The
appropriate parameters were passed in to form the following commands.

./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 1
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 2
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 3
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 4
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 5
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 6
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 7
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 8
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 9
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 10
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 11
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 12
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 13
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 14
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 15
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 16
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 17
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 18
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 19
./iperf3 -c bouygues.testdebit.info -p 5201 -t 5 -P 20

Each of these commands were run three times. Please see written portion for
how parameters were chosen.

"""


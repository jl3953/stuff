#!/usr/bin/python2.7

import argparse
import subprocess
import sys

def run_iperf(parallel, hostname, port=5201, time=5):

    """ Runs the iperf command given in the instructions.

    Args:
        parallel (int): the number of parallel connections with which
            client connects to server.
        hostname (str): host to connect to.
        port (int): port to connect to. Default=5201.
        time (int): time to transmit in seconds. Default=5.

    Returns:
        Return code (int) from subprocess.call command.

    """

    # assuming that iperf3 is in home directory
    command = ["./iperf3",
        "-c", hostname,
        "-p", str(port),
        "-t", str(time),
        "-P", str(parallel)]

    rc = subprocess.call(command)
    print ("rc: [%d] for command: [%s]" % (rc, " ".join(command)))
    sys.stdout.flush()

    return rc


def run_ping(hostname, ping_count=10):

    """ Runs ping command to retrieve RTT.

    Args:
        hostname (str): host to ping.
        ping_count (int): number of times to ping. Default=10.

    Returns:
        Return code (int) of subprocess.call command.

    """

    command = ["ping",
            "-c", str(ping_count),
            hostname]

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

    hosts = ["bouygues.iperf.fr", # France
            "iperf.biznetnetworks.com", # Indonesia
            "iperf.scottlinux.com" # USA
            ]


    for parallel_connections in range(args.min_parallel, args.max_parallel + 1):
        run_iperf(parallel_connections, port=args.port)

    return 0;


if __name__ == "__main__":
    sys.exit(main())


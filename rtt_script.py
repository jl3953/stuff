#!/usr/bin/python2.7

""" This script obtains bandwidth by running iperf3 and RTT by running ping.

For a full list of commands that this script simulated for this assignment,
please refer to the bottom of the script.

Run this script:
    ./rtt_script.py

"""

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


def run_ping(hostname, ping_count=5):

    """ Runs ping command to retrieve RTT.

    Args:
        hostname (str): host to ping.
        ping_count (int): number of times to ping. Default=5.

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

    parser = argparse.ArgumentParser(description="Bandwidth vs rtt.")
    parser.add_argument("--port", "-p", type=int, default=5201,
            help="port to which to connect.")
    args = parser.parse_args()

    hosts = ["bouygues.iperf.fr", # France
            "iperf.biznetnetworks.com", # Indonesia
            "iperf.scottlinux.com", # USA
            "iperf.volia.net", # Ukraine
            "iperf.it-north.net" # Kazakhstan
            ]


    for host in hosts:
        # determine bandwidth
        port = args.port
        run_iperf(1, host, port=args.port)

        # determine rtt
        run_ping(host)

    return 0;


if __name__ == "__main__":
    sys.exit(main())


""" Commands that this script ran for the assignment:

./iperf3 -c bouygues.iperf.fr -p 5201 -t 5 -P 1
ping -c 5 bouygues.iperf.fr 
./iperf3 -c iperf.biznetnetworks.com -p 5201 -t 5 -P 1
ping -c 5 iperf.biznetnetworks.com
./iperf3 -c iperf.scottlinux.com -p 5201 -t 5 -P 1
ping -c 5 iperf.scottlinux.com
./iperf3 -c iperf.volia.net -p 5201 -t 5 -P 1
ping -c 5 iperf.volia.net
./iperf3 -c iperf.it-north.net -p 5201 -t 5 -P 1
ping -c 5 iperf.it-north.net

"""

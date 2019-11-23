#!/usr/bin/env python3

import prometheus_client
import os
import time
import logging
import socket

logger = logging.getLogger(__name__)
HOSTNAME = socket.gethostname()

MON_TEMP = prometheus_client.Gauge('temp', 'Temperature', ['hostname'], namespace='rpi')


def measure_temp():
    output = os.popen("vcgencmd measure_temp").readline().strip()
    return float(output[5:-2])


def update_stats():
    MON_TEMP.labels(HOSTNAME).set(measure_temp())


def main():
    logging.basicConfig(level=logging.INFO)
    prometheus_client.start_http_server(9101)

    while True:
        try:
            update_stats()
        except Exception as ex:
            logger.error("Error updating stats: %s", str(ex))
        time.sleep(5)


if __name__ == '__main__':
    main()

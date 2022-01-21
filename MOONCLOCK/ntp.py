import struct
import time


class NTP:

    TIME1970 = 2208988800

    def __init__(self, socketpool, ntp_servers=None, timeout=30, sleep_between_retries=20):
        self.socketpool = socketpool

        if ntp_servers is None:
            ntp_servers = [
                '0.cz.pool.ntp.org',
                'ntp.nic.cz',
                'tik.cesnet.cz',
                'tak.cesnet.cz',
                'ntp2.muni.cz',
                'ntp.feec.vutbr.cz',
            ]

        self.ntp_servers = ntp_servers
        self.timeout = timeout
        self.sleep_between_retries = sleep_between_retries

    def unixtime(self):
        for ntp_server in self.ntp_servers:
            with self.socketpool.socket(self.socketpool.AF_INET, self.socketpool.SOCK_DGRAM) as sock:
                sock.settimeout(self.timeout)

                try:
                    request_data = '\x1b' + 47 * '\0'
                    sock.sendto(request_data.encode('utf-8'), (ntp_server, 123))

                    response_data = bytearray(48)
                    size = sock.recv_into(response_data)
                    if size != 48:
                        continue

                    unixtime = struct.unpack('!12I', response_data)[10] - self.TIME1970
                except Exception as e:
                    print(e)
                    time.sleep(self.sleep_between_retries)
                    continue

                return unixtime


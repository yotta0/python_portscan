import sys
import socket


class PortScan:
    """Scan network ports of a IP Address

    Read ip addressa start and end range
    in sys args then scan that
    range for open network ports

    Attributes:
        ip_addr: a string containing IP address
        start_addr: integer containing start range of the scan
        end_addr: integer containing end range of the scan
    """
    def __init__(self, args=list):
        """Inits PortScan Class"""
        self.ip_addr = args[1]
        self.start_addr = int(args[2])
        self.end_addr = int(args[3])

    def _scan_ports(self):
        for port in range(self.start_addr, self.end_addr):
            print(f'Scanning Port {port} ')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if sock.connect_ex((self.ip_addr, port)) == 0:
                print(f"Port open at {port}")
                sock.close()

    def run_scan(self):
        self._scan_ports()


if __name__ == '__main__':
    PortScan(sys.argv).run_scan()

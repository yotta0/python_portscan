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
        """Scan ports of a IP Address
        """
        open_ports_list = []
        for port in range(self.start_addr, self.end_addr):
            print(f'Scanning Port {port} ')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if sock.connect_ex((self.ip_addr, port)) == 0:
                open_ports_list.append(port)
                print(f"Port open at {port}")
                sock.close()
        self._log_to_file(open_ports_list)

    def _log_to_file(self, open_ports):
        """Log open ports to a file
        """
        for port in open_ports:
            with open('open_ports.txt', 'a') as f:
                f.write(f'Port {port} is open\n')

    def run_scan(self):
        self._scan_ports()


if __name__ == '__main__':
    PortScan(sys.argv).run_scan()

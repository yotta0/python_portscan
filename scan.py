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
    def __init__(self, ip_addr=str, start_addr=int, end_addr=int):
        """Inits PortScan Class"""
        self.ip_addr = ip_addr
        self.start_addr = int(start_addr)
        self.end_addr = int(end_addr)


    def _scan_ports(self):
        for port in range(self.start_addr, self.end_addr):
            print(f'Scanning Port {port} ')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if sock.connect_ex((self.ip_addr, port)) == 0:
                print(f"Port open at {port}")
                sock.close()




if __name__ == '__main__':
    PortScan(sys.argv[1], sys.argv[2], sys.argv[3])._scan_ports()

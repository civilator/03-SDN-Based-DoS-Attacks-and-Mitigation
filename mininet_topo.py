from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def create():
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    info('--controller\n')
    net.addController('c0', controller=RemoteController,
                      ip='127.0.0.1', port=6655)

    info('--switch\n')
    s1 = net.addSwitch('s1', protocols='OpenFlow10')

    info('--hosts\n')
    h1 = net.addHost('h1', ip='192.168.2.10/24', mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', ip='192.168.2.20/24', mac='00:00:00:00:00:02')
    h3 = net.addHost('h3', ip='192.168.2.30/24', mac='00:00:00:00:00:03')
    h4 = net.addHost('h4', ip='192.168.2.40/24', mac='00:00:00:00:00:04')

    info('--links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)

    info('--starting network\n')
    net.start()

    info('--connectivity\n')
    net.pingAll()

    CLI(net)

    info('--stopping network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    create()

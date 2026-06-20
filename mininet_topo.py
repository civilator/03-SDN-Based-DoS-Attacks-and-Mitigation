#!/usr/bin/env python3
# mininet_topo.py
# CSE 548 - SDN-Based DoS Attacks and Mitigation (Project 3)
# Plain Mininet topology (4 hosts, 1 OVS switch, 1 remote controller).
# Reused from Project 2 with fixed MAC addresses added so the firewall
# configs and the assignment's MAC<->IP table stay consistent.
#
#   Host  IP               MAC                 role
#   h1    192.168.2.10/24  00:00:00:00:00:01   attacker
#   h2    192.168.2.20/24  00:00:00:00:00:02   victim
#   h3    192.168.2.30/24  00:00:00:00:00:03
#   h4    192.168.2.40/24  00:00:00:00:00:04
#
# Run order:
#   Terminal 1:  cd ~/pox && sudo ./pox.py openflow.of_01 --port=6655 \
#                   forwarding.l3_learning pox.forwarding.L3Firewall \
#                   --l2config=l2firewall.config --l3config=l3firewall.config
#   Terminal 2:  sudo python3 mininet_topo.py

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

#!/usr/bin/env python3
# mininet_topo_9hosts.py
# CSE 548 - SDN-Based DoS Attacks and Mitigation (Project 3)
# 9-host variant for the Task 2 walkthrough (the graded deliverable uses
# the 4-host mininet_topo.py). One OVS switch (s1), one remote controller.
#
#   Host  IP               MAC                 role
#   h1    192.168.2.10/24  00:00:00:00:00:01   attacker
#   h2    192.168.2.20/24  00:00:00:00:00:02   victim
#   h3    192.168.2.30/24  00:00:00:00:00:03
#   h4    192.168.2.40/24  00:00:00:00:00:04
#   h5    192.168.2.50/24  00:00:00:00:00:05
#   h6    192.168.2.60/24  00:00:00:00:00:06
#   h7    192.168.2.70/24  00:00:00:00:00:07
#   h8    192.168.2.80/24  00:00:00:00:00:08
#   h9    192.168.2.90/24  00:00:00:00:00:09
#
# Run order:
#   Terminal 1:  cd ~/pox && sudo ./pox.py openflow.of_01 --port=6655 \
#                   forwarding.l3_learning pox.forwarding.L3Firewall \
#                   --l2config=l2firewall.config --l3config=l3firewall.config
#   Terminal 2:  sudo python3 mininet_topo_9hosts.py

from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

NUM_HOSTS = 9


def create():
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    info('*** Adding controller\n')
    net.addController('c0', controller=RemoteController,
                      ip='127.0.0.1', port=6655)

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1', protocols='OpenFlow10')

    info('*** Adding hosts\n')
    hosts = []
    for i in range(1, NUM_HOSTS + 1):
        ip = '192.168.2.%d/24' % (i * 10)        # h1=.10, h2=.20, ... h9=.90
        mac = '00:00:00:00:00:%02x' % i           # 00:00:00:00:00:01 ... :09
        hosts.append(net.addHost('h%d' % i, ip=ip, mac=mac))

    info('*** Creating links\n')
    for h in hosts:
        net.addLink(h, s1)

    info('*** Starting network\n')
    net.start()

    info('*** Testing connectivity\n')
    net.pingAll()

    CLI(net)

    info('*** Stopping network\n')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    create()

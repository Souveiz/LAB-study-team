import xml.dom.minidom
from ncclient import manager
m = manager.connect(
 host="192.168.56.102",
 port=830,
 username="cisco",
 password="cisco123!",
 hostkey_verify=False
 )
n = manager.connect(
 host="192.168.56.103",
 port=830,
 username="cisco",
 password="cisco123!",
 hostkey_verify=False
 )

#print("#Supported Capabilities (YANG models):")
#for capability in m.server_capabilities:
#    print(capability)

#netconf_reply = m.edit_config(target="running", config=netconf_newloop)


# Attempted OSPF, it runs without error, XML shows configuration done, but does not show on the router!
netconf_ospf1 = '''
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <router>
                    <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                        <id>1</id>
                        <router-id>1.1.1.1</router-id>
                        <network>
                            <ip>10.0.0.0</ip>
                            <mask>0.0.0.255</mask>
                            <area>0</area>
                        </network>
                    </ospf>
                </router>
            </native>
        </config>
'''

netconf_ospf2 = '''
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <router>
                    <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                        <id>1</id>
                        <router-id>2.2.2.2</router-id>
                        <network>
                            <ip>10.0.0.0</ip>
                            <mask>0.0.0.255</mask>
                            <area>0</area>
                        </network>
                    </ospf>
                </router>
            </native>
        </config>
'''




netconf_reply2 = m.edit_config(target="running", config=netconf_ospf1)
print(xml.dom.minidom.parseString(netconf_reply2.xml).toprettyxml())

netconf_reply3 = n.edit_config(target="running", config=netconf_ospf2)
print(xml.dom.minidom.parseString(netconf_reply3.xml).toprettyxml())

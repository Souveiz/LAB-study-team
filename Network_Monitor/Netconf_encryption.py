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
netconf_key_encryption = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <password>
 <encryption>
 <aes>
 </aes>
 </encryption>
 </password>
 </native>
</config>
"""




netconf_reply2 = m.edit_config(target="running", config=netconf_key_encryption)
print(xml.dom.minidom.parseString(netconf_reply2.xml).toprettyxml())

netconf_reply3 = n.edit_config(target="running", config=netconf_key_encryption)
print(xml.dom.minidom.parseString(netconf_reply3.xml).toprettyxml())



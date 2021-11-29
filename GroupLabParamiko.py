import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient() #Creating an ssh client object
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass('Enter Password:')
router1 = {'hostname': '172.16.0.1', 'port': '22', 'username':'cisco', 'password':'cisco'}
router2 = {'hostname': '172.16.0.2', 'port': '22', 'username':'cisco', 'password':'cisco'}
routers = [router1, router2]

for router in routers:
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('cisco\n')
    shell.send('sh cdp neighbors\n')
    time.sleep(2)

    output = shell.recv(10000).decode()
    print(output)

if print(ssh_client.get_transport().is_active()) == True:
    print('Closing Connection')
    ssh_client.close()

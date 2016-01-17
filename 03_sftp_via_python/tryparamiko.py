import os
import paramiko



hostname = '192.168.199.189'
username = 'pi'
password = 'raspberry'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
sftp = ssh.open_sftp()

# Updated code below:
def rm(path):
    files = sftp.listdir(path)

    for f in files:
        filepath = os.path.join(path, f)
        try:
            sftp.remove(filepath)
        except IOError:
            rm(filepath)

    sftp.rmdir(path)
rm('/home/pi/Desktop/myfolder')

# Close to end
sftp.close()
ssh.close()

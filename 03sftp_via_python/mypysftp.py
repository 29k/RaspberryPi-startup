import pysftp

hostname = '10.6.0.74'
username = 'pi'
password = 'raspberry'

targetFolder = '/home/pi/Desktop/'
createFolder = 'myfolder'

sftp = pysftp.Connection(hostname, username, password)



sftp.close()

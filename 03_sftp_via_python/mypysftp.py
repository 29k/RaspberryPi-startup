import pysftp

hostname = '10.6.0.76'
username = 'pi'
password = 'raspberry'
print hostname, username,password

targetFolder = '/home/pi/Desktop/'
createFolder = 'myfolder'

cinfo = {'host':hostname, 'username':username, 'password':password, 'port':2222}
print cinfo
with pysftp.Connection(**cinfo) as sftp:
    try:
        sftp.makdirs('/home/pi/Desktop/myfolder')
    except:
        sftp.cwd('/home/pi/Desktop/myfolder')



sftp.close()

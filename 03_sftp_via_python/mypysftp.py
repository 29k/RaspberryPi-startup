import pysftp

hostname = '192.168.199.189'
username = 'pi'
password = 'raspberry'
print hostname, username,password

targetFolder = '/home/pi/Desktop/'
createFolder = 'myfolder'
disFolder = targetFolder + createFolder

sourceFolder = '/Users/yangyikai/Desktop/webproject/PM-sop/SOP/08_production/08_01/08_01_02_coding'

sftp = pysftp.Connection(hostname, username=username, password=password)
sftp.cwd(targetFolder)
print '==>move into folder' + targetFolder

try:
    sftp.mkdir('myfolder', mode=777)
    print '==>create file: ' + createFolder
except:
    print '==>file myfolder already exist, delete it first'
    sftp.rmdir('myfolder')
    print '==>delete folder' + createFolder
    sftp.mkdir('myfolder/*', mode=777)
    print '==>create file: ' + createFolder
print '==>source file: ' + sourceFolder
try:
    sftp.put_r(sourceFolder, disFolder, preserve_mtime=True)
    print '==>Copy file OK'
except:
    pass

#try:
#     sftp.makdirs(targetFolder)
#     print 'create file'
# except:
#     sftp.rmdir(targetFolder)
#     print 'delete file'
#     sftp.makdirs(targetFolder)
#     print 'and create file'
print sftp.pwd
print sftp.listdir()

sftp.close()

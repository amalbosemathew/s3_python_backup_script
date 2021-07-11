from secrets import access_key,secret_key
import os
import tarfile
import boto3
import datetime
import posixpath

directory = "./docroot/"
#Local backup location
temp_back = "/tmp/backup/"

for item in os.listdir(directory):
    
  #retreving the current date  
  dt = datetime.datetime.now()
    
  #Modifying according to our preffered date-time format .
  ts = dt.strftime('%d-%m-%Y-%H-%M')
    
  absPath = posixpath.join(directory,item)
  tarName = '{}{}-{}.tar.gz'.format(temp_back,item,ts)

  #Lets create the tar file with .gz  
  tar = tarfile.open(tarName,'w:gz')
    
  tar.add(absPath)
  #Creating the tar file.
    
  tar.close()
  print('Backup for',absPath,'created')
print()

client = boto3.client('s3',aws_access_key_id= access_key,aws_secret_access_key = secret_key)

for file in os.listdir('/tmp/backup'):
    if '.tar' in file:
        upload_file_bucket = "private.s3.bucket.com"
        upload_file_key    =  "backup/{}".format(file)
        path = posixpath.join('/tmp/backup/',file)
        #Lets upload the tar file to s3 bucket.
        client.upload_file(path,upload_file_bucket,upload_file_key)
        print('Upload to S3 successfull for',file)

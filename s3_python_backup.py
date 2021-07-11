from secrets import access_key,secret_key
import os
import tarfile
import boto3
import datetime
import posixpath

directory = "./docroot/"

for item in os.listdir(directory):
    
  dt = datetime.datetime.now()

  ts = dt.strftime('%d-%m-%Y-%H-%M')
    
  absPath = posixpath.join(directory,item)

  tarName = '/tmp/backup/{}-{}.tar.gz'.format(item,ts)
   
  tar = tarfile.open(tarName,'w:gz')
    
  tar.add(absPath)
 
  tar.close()
  print('Backup for',absPath,'created')
print()

client = boto3.client('s3',aws_access_key_id= access_key,aws_secret_access_key = secret_key)
for file in os.listdir('/tmp/backup'):
    if '.tar' in file:
        upload_file_bucket = "private.s3.bucket.com"
        upload_file_key    =  "backup/{}".format(file)
        path = posixpath.join('/tmp/backup/',file)
        client.upload_file(path,upload_file_bucket,upload_file_key)
        print('Upload to S3 successfull for',file)

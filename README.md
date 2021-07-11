# Python Script for uploading files to S3 bucket
[![Builds](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

---
# Description

Here I would like to demonstrate a simple python script to take the backup of each directories in your Document Root in tar.gz file extension with date and time appended and then upload the same backup files to the S3 bucket. 

---

# Features

- Simple and easy to manage backup and to upload the same to S3.
---
# Prerequisites

- Need to have S3 bukcet create.
- Need to have Boto3 installed in your machine.
- IAM role with attached policies for accesing S3.

---
# Installation 

- [Boto3 Installation]("https://pypi.org/project/boto3/")
---
# How to clone this repository and execute in Ansible master.
_Steps:_
```sh
1. Create secrets.py with access_key and secrets_key of the IAM programatic user access with S3 full access.
2. Copy the s3_python_backup.py the same directory.
3. Modify the "directory" name as per your requirement.
4. Modify the "temp_back" name  as per your preference to save the backup locally.
5. Execute the script. 
BINGO !!!
```

# Conclusion

The intention of this project is to create backups of the directories in the document root and to upload the same to S3 bucket.

Please feel free to contact me. Any type of feedbacks are appreciated.
<p align="center">
<a href="mailto:mathew.amalbose@gmail.com"><img src="https://img.shields.io/badge/-mathew.amalbose@gmail.com-D14836?style=flat&logo=Gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/amal-bose-mathew"><img src="https://img.shields.io/badge/-Linkedin-blue"/></a>
<a href="https://techbit-new.blogspot.com/"><img src="https://img.shields.io/badge/-Blogger-orange"/></a>
  


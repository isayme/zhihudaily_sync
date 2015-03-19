#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qiniu import Auth, put_file

# AK = Access Key 
AK = ''
# SK = Secret Key
SK = ''
# BN = Bucket Name
BN = ''


def upload_file(local_path, remote_path = None, mime_type = None):
    q = Auth(AK, SK)

    if not remote_path:
        remote_path = local_path
    
    token = q.upload_token(BN, remote_path)
    
    ret, info = put_file(token, remote_path, local_path, mime_type=mime_type)
    if not ret or 200 != info.status_code:
        print 'Error upload:', local_path, 'to', remote_path
        print ret, info
        
    return (ret, info)
    
if __name__ == '__main__':
    upload_file('ss.jpg', 'ss.jpg')
    
    

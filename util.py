#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2
import urlparse

from qnu import upload_file

def download(url, upload=True, check_exists=True, prefix=''):
    path = prefix + urlparse.urlparse(url).path[1:]
    dir = os.path.dirname(path) or '.'
    
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    suffix = os.path.splitext(path)[1]
    path = path + ('' if suffix else '.json')
    
    if check_exists and os.path.exists(path):
        print path, 'exists'
        with open(path, 'rb') as f:
            data = f.read()
    else:
        print path, 'not found'
        opener = urllib2.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0'),
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
        ]
        data = opener.open(url).read()   
        with open(path, 'wb') as f:
            f.write(data)
    
    if upload:
        upload_file(path, path)
    
    return data
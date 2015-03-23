#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from util import download

if __name__ == '__main__':
    data = download('http://news.at.zhihu.com/api/2/news/latest', check_exists=False)    
    jd = json.loads(data)
    for item in jd['news']:
        download(item['image'], prefix=(jd['date']+'/'))
    
    # http://news.at.zhihu.com/api/2/news/before/20131119
    if not os.path.exists('api/2/news/before/' + jd['date'] + '.json'):
        data = download('http://news.at.zhihu.com/api/2/news/before/' + jd['date'])
        jd = json.loads(data)
        for item in jd['news']:
            download(item['image'], prefix=(jd['date']+'/'))

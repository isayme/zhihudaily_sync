#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time
import datetime
from util import download

if __name__ == '__main__':
    data = download('http://news.at.zhihu.com/api/2/news/latest', check_exists=False, upload=False)    
    jd = json.loads(data)
    date = datetime.date(int(jd['date'][:4]), int(jd['date'][4:6]), int(jd['date'][6:]))
    
    while date >= datetime.date(2013, 5, 19):
        url = 'http://news.at.zhihu.com/api/2/news/before/' + date.strftime("%Y%m%d")
        print url

        if not os.path.exists('api/2/news/before/' + date.strftime("%Y%m%d") + '.json'):
            data = download(url)
            jd = json.loads(data)
            for item in jd['news']:
                download(item['image'], prefix=(jd['date']+'/'))
            time.sleep(60*30);
        else:
            print 'Exists:', url
        
        date = date + datetime.timedelta(-1)
        
        
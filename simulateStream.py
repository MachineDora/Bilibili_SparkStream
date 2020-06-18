# -*- coding:utf-8 -*-
import time
import pymongo
import shutil
import datetime

# get the date between them
def get_every_day(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

if __name__ == '__main__':

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.bilibili
    col = db.videosAhead
    col2=db.videos

    dateDuration = get_every_day('2018-12-20', '2018-12-31')

    result = 0

    for oneDate in dateDuration:
        fileName = oneDate+ "&" + str(time.time())
        filePath = r'tmp/' + str(fileName) + '.log'
        with open(filePath, 'w',errors='ignore',encoding='utf-8') as f:
            queryAns = col.find({'time': {"$regex": oneDate}})

            for doc in queryAns:
                list=doc['key']
                for item in list:
                    f.write(item)
                    f.write('\n')
                    result+=1
                    print(result)
        destination = shutil.move(filePath, r'log/' + str(fileName) + '.log')
        time.sleep(0.5)

    dateDuration2=get_every_day('2019-01-01','2019-04-01')

    for oneDate in dateDuration2:
        fileName = oneDate+ "&" + str(time.time())
        filePath = r'tmp/' + str(fileName) + '.log'
        with open(filePath, 'w',errors='ignore',encoding='utf-8') as g:
            queryAns = col2.find({'time': {"$regex": oneDate}})

            for doc in queryAns:
                list=doc['key']
                for item in list:
                    g.write(item)
                    g.write('\n')
                    result+=1
                    print(result)
        destination = shutil.move(filePath, r'log/' + str(fileName) + '.log')
        time.sleep(1)


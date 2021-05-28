import time
from datetime import datetime, timedelta
from threading import Timer
from scrapy.crawler import CrawlerProcess
from webCrawl.spiders.WebCrawlSpider import WebCrawlSpider
import os
import pymysql.err
import psutil


def runWebCrawlSpider():
    try:
        connection = pymysql.connect(host='localhost', user='root', password='root', database="webcrawl")
        if connection is not None:
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)

            cursor = connection.cursor()
            try:
                sql = "select * from webcrawl.webcrawlui_cities limit 2"
                n_cities = cursor.execute(sql)
                cities = cursor.fetchall()

                for city in cities:
                    command = 'curl http://localhost:6800/schedule.json -d project=webCrawl -d spider=googleSearch -d city="' + city[1]+ '" -d state="'+ city[3] +'"'
                    os.system(command)

            except pymysql.err.DatabaseError as e:
                print("Error while getting weblinks: ", str(e))
    except:
        print("Error while connecting to MySQL for cities retrieval")
    finally:
        if (connection is not None):
            cursor.close()
            connection.close()
            print("MySQL connection is closed for weblinks retrieval")



if __name__ == "__main__":

    current_time = datetime.today()
    next_run_time = current_time.replace(day=current_time.day + 1, hour=1, minute=0, second=0, microsecond=0)
    delta = next_run_time - current_time
    secs = delta.seconds

    secs = 1
    print(current_time)
    print(next_run_time)

    while True:
        scrapy_running = False
        for proc in psutil.process_iter():
            if proc.name().lower().find("scrapy") != -1:
                scrapy_running = True
                print(proc.name().lower())
                break

        if not scrapy_running:
            print("Scrapyd is not started. Starting scrapyd now..........")
            os.system("start scrapyd")
            continue

        print("current time: %s" %(datetime.today()))
        print("Going on sleep for %s seconds. Next run is at %s" % (secs, (datetime.today() + timedelta(0, secs))))
        time.sleep(secs)
        runWebCrawlSpider()
        current_time = datetime.today()
        next_run_time = current_time.replace(day=current_time.day+1, hour=1, minute=0, second=0, microsecond=0)
        delta = next_run_time - current_time
        secs = delta.seconds
        secs = 100
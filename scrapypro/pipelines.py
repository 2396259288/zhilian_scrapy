# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
# from django.conf import settings 

class ScrapyproPipeline(object):
    def __init__(self):
        self.f = open("jobs.json", 'wb')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii = False)+', \n'
        self.f.write(content.encode('utf-8'))
        return item
    def close_spider(slef, spider):
        slef.f.close()

class CitysPipeline(object):
    def __init__(self):
        self.f = open("citys.json", 'wb')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii = False)+', \n'
        self.f.write(content.encode('utf-8'))
        return item
    def close_spider(slef, spider):
        slef.f.close()




class NewsPipeline(object):
    def __init__(self):
        self.f = open("news.json", 'wb')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii = False)+', \n'
        self.f.write(content.encode('utf-8'))
        return item
    def close_spider(slef, spider):
        slef.f.close()


class zlJobPipeline(object):
    def __init__(self):
        self.f = open("zljobs.json", 'wb')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii = False)+', \n'
        self.f.write(content.encode('utf-8'))
        return item
    def close_spider(slef, spider):
        slef.f.close()



class saveMysqlPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(host='127.0.0.1', port = 3306, db='scrapy_db', user='root', passwd='123456', charset='utf8', use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute(
                "insert into index_jobinfo(name, salary, companyName,companySize,companyType,workingExp,city ,time,idName,url,info,companyEmail) values (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(item['name'],item['salary'], item['companyName'],item['companySize'],item['companyType'],item['workingExp'],item['city'],item['time'],item['idName'],item['url'],item['info'],item['email']))

            # 提交sql语句
            self.connect.commit()
            print("--------------------------------------------------------------------------------")
            print ('存入数据库成功')
            print("--------------------------------------------------------------------------------")

        except Exception as e:
            # 出现错误时打印错误日志
            print("--------------------------------------------------------------------------------")
            print (e)
            print("--------------------------------------------------------------------------------")
        return item


class saveMysqlPipeline1(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(host='127.0.0.1', port = 3306, db='scrapy_db', user='root', passwd='123456', charset='utf8', use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute(
                "insert into company(company_name, company_features, has_labels,industry_field,city, company_size,company_url) values (%s, %s,%s, %s, %s, %s, %s);",(item['company_name'],item['company_features'], item['has_labels'],item['industry_field'],item['city'],item['company_size'],item['company_url']))

            # 提交sql语句
            self.connect.commit()
            print("--------------------------------------------------------------------------------")
            print ('存入数据库成功')
            print("--------------------------------------------------------------------------------")

        except Exception as e:
            # 出现错误时打印错误日志
            print("--------------------------------------------------------------------------------")
            print (e)
            print("--------------------------------------------------------------------------------")
        return item

  
class saveMysqlPipeline2(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(host='127.0.0.1', port = 3306, db='scrapy_db', user='root', passwd='123456', charset='utf8', use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute(
                "insert into tb_position(position_category, positon_name, position_nature,salary_min,salary_max,city, experience,education ,position_advantage,position_address,position_desc,update_time) values (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(item['position_category'],item['positon_name'], item['position_nature'],item['salary_min'],item['salary_max'],item['city'],item['experience'],item['education'],item['position_advantage'],item['position_address'],item['position_desc'],item['update_time']))

            # 提交sql语句
            self.connect.commit()
            print("--------------------------------------------------------------------------------")
            print ('存入数据库成功')
            print("--------------------------------------------------------------------------------")

        except Exception as e:
            # 出现错误时打印错误日志
            print("--------------------------------------------------------------------------------")
            print (e)
            print("--------------------------------------------------------------------------------")
        return item
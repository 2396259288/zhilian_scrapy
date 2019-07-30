# -*- coding: utf-8 -*-
import scrapy, os, json

import tkinter
from tkinter import messagebox
# from os import *


class weiboSpider(scrapy.Spider):
    name = 'weibohot'    
    start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=filter_type%3Drealtimehot%26mi_cid%3D100103%26pos%3D0_0%26c_type%3D30%26display_time%3D1561469752&luicode=10000011&lfid=231583']
    def parse(self, response):
        tk = tkinter.Tk()
        tk.geometry('1366x768')
        hotnews = []        
        try:
            data = json.loads(response.text)
            rts = data['data']['cards'][0]['card_group']
            print(rts)
            for rt in rts[1:]:
                dict = {}
                dict[rt['desc']] = str(rt['desc_extr'])    
                print(dict)
                hotnews.append(dict)

            listbox = tkinter.Listbox(tk, font = ('default', 18), width = 1366, height = 768)
            for item in hotnews:
                listbox.insert(tkinter.END, item)

            listbox.pack()
            tk.mainloop()
            # messagebox.showinfo('微博头条', hotnews)
                # try:
                #     f = open('d:/weibohot.json','ab+')
                #     content = json.dumps(dict, ensure_ascii = False)
                #     f.write(content.encode('utf-8'))
                #     f.write(b'\n')
                #     f.close()
                # except Exception as e:
                #     print('+'*10 , e)
        except Exception as e:
            print('-'*10 , e)


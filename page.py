from email import message
from multiprocessing.sharedctypes import Value
from os import access
import facebook as fb
import tempfile
import sys
import os
import pandas
import gspread
gc = gspread.service_account(filename='cre.json')
sh = gc.open('DuLieu').sheet1
for i in range(1):
    gg=sh.acell('C2').value

    print(gg)
    access_token="EAALFoxXSzz8BANikRSntHoIOyX9zxJrYT3U2bhDTJZCEG9ctS9CpvY8jIsoVOxDykwEsKczZAbLZAUVYT6L4vmZAAWlAxvjuvuDV5slfvhijNkGJsWdI9NXDWZBZCb75qkoaC94ZCxLhtji2h5qg6Hr9n25Vf6ciVlDr6ZBcCdANwjZAGRUt27leMnSiiosj3ATGj1mYHwwQId0AercFH8ZCcA"
    asafb=fb.GraphAPI(access_token)
    dang=asafb.put_photo(image=open("kt.jpg",'rb'),message=gg)
    # laydulieu=asafb.get_object("me?fields=name,link")
    # print(laydulieu)
    print("đã Đăng")

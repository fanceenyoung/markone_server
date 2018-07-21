# -*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.
"""
import requests
name='first'
nickname='first nickname'
email='first@126.com'
password='first'
data = {
    'name': name,
    'nickname': nickname,
    'email': email,
    'password': password,
}
# post_url='http://18.191.203.74:11112/api/users/'
post_url='http://127.0.0.1:8000/api/users/'
resp=requests.post(post_url, json=data)


from app.models import *
user=User.objects.first()
note = Notes.objects.first()
note=Notes.objects.create(user=user, title='user2 notes', origin='http://www.google.com')

section1=Sections.objects.create(notes=note, user=user, remark='user2 section1')
section2=Sections.objects.create(notes=note, user=user, remark='user2 section2')
section3=Sections.objects.create(notes=note, user=user, remark='user2 section3')


import requests
name='first'
nickname='first nickname'
email='first@163.com'
password='first'
data = {
    'remark': '具体的笔记段落，text文本存储',
    'origin': 'http://www.baidu.com',
    'notes': {'uuid': '22149a5a-f356-418d-be65-cc4a34dc397c'},
    'user': {'uuid': '207d01e68f0b4a818cbb5ef9ccf19c31'},
}
post_url='http://127.0.0.1:8000/api/sections'
resp=requests.post(post_url, json=data)

"""
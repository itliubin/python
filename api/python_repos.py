#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:python_repos.py
@date:2019/6/25_11:21

'''

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status code:', r.status_code)

response_dict = r.json()
print(response_dict.keys())
print("Total respositories:",response_dict['total_count'])

repo_dicts = response_dict['items']
print("Resposigtories returned:",len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKEYS:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)


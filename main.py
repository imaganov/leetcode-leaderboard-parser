import requests

r = requests.get('https://leetcode.com/contest/weekly-contest-176/ranking')

print(r.text)
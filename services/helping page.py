import requests
from lxml import html
from lxml import etree


url = "http://www.finmarket.ru/currency/rates/"

payload={}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': '_ym_uid=1681144816958865930; _ym_d=1681144816; _ym_visorc=w; adtech_uid=d9a94228-c5cd-4e3b-aea8-1dde3e0e4fa7%3Afinmarket.ru; top100_id=t1.7919.724931502.1681144815722; last_visit=1681130415725%3A%3A1681144815725; t3_sid_7919=s1.1362791205.1681144815724.1681144815728.1.2; _ym_isad=1; tmr_lvid=c304bba83abeee660bc1ab447d43559b; tmr_lvidTS=1681144815966; tmr_detect=1%7C1681144815985',
  'If-Modified-Since': 'Sun, 10 Apr 2023 13:40:14 GMT',
  'Referer': 'https://www.google.com/',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}


response = requests.request("GET", url, headers=headers, data=payload)

tree = html.fromstring(response.text)
usd = etree.tostring(tree.xpath('/html/body/div[7]/div[7]/div[2]/div[7]/table/tbody/tr[14]/td[4]')[0])[4:11].decode('utf-8')
eur = etree.tostring(tree.xpath('/html/body/div[7]/div[7]/div[2]/div[7]/table/tbody/tr[15]/td[4]')[0])[4:11].decode('utf-8')
gel = etree.tostring(tree.xpath('/html/body/div[7]/div[7]/div[2]/div[7]/table/tbody/tr[11]/td[4]')[0])[4:11].decode('utf-8')
print(usd, eur, gel)

print(usd)

# print(response.text)
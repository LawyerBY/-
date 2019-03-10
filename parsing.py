import requests
from lxml.html import etree
site_body = requests.get('http://afisha.yandex.by/minsk')
html = """\
analysis = [site_body.text][0]
root = etree.fromstring(html)
print(root.xpath('//span[@class="card_info_inner"]')[0].text)
print(analysis)
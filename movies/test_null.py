# Filename: test_null.py

import getDouban_module

url = 'http://movie.douban.com/tag/%E6%96%B0%E6%B5%B7%E8%AF%9A'
html = getDouban_module.getHtml(url)
# print html
pages = getDouban_module.getTotalPage(html)
print pages


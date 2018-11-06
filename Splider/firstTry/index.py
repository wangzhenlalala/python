import re
from urllib import request
import pprint

def craw(url, page):
    html1 = request.urlopen(url).read()
    html1 = str(html1)
    pattern1 = r'<div id="plist" .+?<div class="page clearfix">'
    result1 = re.compile(pattern1).findall(html1)
    result1 = result1[0]
    img_pattern = r'<img width="220" height="220".+? src="(.+?\.jpg)"\s*/?>'
    img_re = re.compile(img_pattern)
    result2 = img_re.findall(result1)
    pprint.pprint(result2)

if __name__ == '__main__':
    url = "https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"
    craw(url, 1)
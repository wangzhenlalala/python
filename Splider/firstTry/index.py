import re
from urllib import request
import pprint
from subprocess import Popen, PIPE
# tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
file = open('./text.html', 'wb')

def craw(url, page):
    html1 = request.urlopen(url).read() #binary
    file.write(html1)
    file.close()
    html1 = str(html1)
    
    pattern1 = r'<div id="plist" .+?<div class="page clearfix">'
    result1 = re.compile(pattern1).findall(html1) 
    result1 = result1[0]    #找到包含 img的最外层 div
    img_pattern = r'<img.+?width="220".*?src="(.+?\.(jpg|png))"\s*?\/?>'
    img_re = re.compile(img_pattern)
    result2 = img_re.findall(result1)
    for item in result2:
        print(len(item[0]), item[1][0:5])
    print(len(result2))
if __name__ == '__main__':
    url = "https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"
    craw(url, 1)
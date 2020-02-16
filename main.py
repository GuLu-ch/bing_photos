import requests
import re
import time

def get_img():
    
    url = "https://cn.bing.com"
    r = requests.get(url)
    #print(r.text)

    pattern = 'href="(.*?)&'
    img_url = url + re.search(pattern,r.text).group(1)
    #print(img_url)
    '''
    pattern = 'id=(.*?).jpg'
    img_name = re.search(pattern,img_url).group(1)
    #print(img_name)
    '''
    
    img_data =  requests.get(img_url)
    
    time_now = time.strftime("%Y-%m-%d", time.localtime())
    
    img_f = open(time_now+'.jpg','wb')
    img_f.write(img_data.content)
    
    img_f.close()
    return time_now


print(get_img())
    

    




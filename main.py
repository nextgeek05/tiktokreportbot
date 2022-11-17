import requests
import os 
enable_proxy=str(input("Use Proxies (SOCKS5)? (yes or no): "))
report_link=str(input("input tiktok report link from inspect element: "))
n=0
def importproxy(n):
    with open('proxies.txt') as f:
        lines = f.readlines()[n]
        lines="socks5://"+str(lines)
        return(lines)
if enable_proxy=="yes":
    proxy_enabled=True
else:
    proxy_enabled=False
while True:
    if proxy_enabled==False:
        r=requests.get(report_link)
        print(str(r.text) + str("     Report n: ")+ str(n))
        n=n+1
    else:
        proxy=importproxy(n)
        proxies={
            'https' : proxy
        }
        try:
            r=requests.get(report_link, proxies=proxies)
            print(str(r.text) + str("     Report n: ")+ str(n))
            n=n+1
        except (requests.exceptions):
            print("Proxy Error, check your proxy list............. Skipping proxy")

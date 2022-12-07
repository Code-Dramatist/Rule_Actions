from urllib.request import proxy_bypass
import requests
import os
import time
import shutil
loon_rule_url = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/"
reject_dict = {
    "anti-ad-surge2": "https://raw.githubusercontents.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt",
    "AdGuardSDNSFilter_Domain": loon_rule_url+"AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list",
    "Privacy": loon_rule_url+"Privacy/Privacy.list",
    "Privacy_Domain": loon_rule_url+"Privacy/Privacy_Domain.list"
}
proxy_dict = {
    "GlobalMedia": loon_rule_url+"GlobalMedia/GlobalMedia.list",
    "GlobalMedia_Domain": loon_rule_url+"GlobalMedia/GlobalMedia_Domain.list",
    "Global": loon_rule_url+"Global/Global.list",
    "Global_Domain": loon_rule_url+"Global/Global_Domain.list",
    "Proxy":loon_rule_url+"Proxy/Proxy.list",
    "Proxy_Domain":loon_rule_url+"Proxy/Proxy_Domain.list"
}
direct_dict = {
    "ChinaMax": loon_rule_url+"ChinaMax/ChinaMax.list",
    "ChinaMax_Domain": loon_rule_url+"ChinaMax/ChinaMax_Domain.list",
}

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
def load_file(Dictionary,file_way):
    if not os.path.exists(file_way):
        os.mkdir(file_way)
    for key in Dictionary:
        _ = requests.get(Dictionary[key],headers=header).text
        with open("./"+file_way+"/"+key+".list", "w") as f:
            f.write(_)
        f.close()
        time.sleep(1)

def remove():
    shutil.rmtree("reject_dict")
    shutil.rmtree("proxy_dict")
    shutil.rmtree("direct_dict")

if __name__ == '__main__':
    remove()
    load_file(reject_dict,"Reject_Rule")
    load_file(proxy_dict,"Proxy_Rule")
    load_file(direct_dict,"Direct_Rule")

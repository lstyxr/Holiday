import requests
import str2header
import json
import datetime
from datetime import timedelta
import time
  
now = datetime.datetime.now()

url = "https://aflow.dingtalk.com/dingtalk/web/query/instdata/saveDataExportJobForInstances.json"

headers = '''
authority: aflow.dingtalk.com
method: POST
path: /dingtalk/web/query/instdata/saveDataExportJobForInstances.json
scheme: https
_csrf_token_: 1640077106082
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
client-corpid: dingcc3c8a50fc75c24dffe93478753d9884
content-length: 223
content-type: application/x-www-form-urlencoded; charset=UTF-8
cookie: arms_uid=e9f07a1f-9cb3-4191-a6e0-0857115d1606; cna=OE8/GqCuOyUCAbfmCgVdIMdE; xlly_s=1; cmouse=sdbd2734a-e535-4815-a401-18b05c9a9f63-1640050272757; dt_org=103332353; dd_n=CN; UM_distinctid=17dda9d3bf01c0-078824301d616-57b193e-1fa400-17dda9d3bf136d; dingtalk_corpid=dingcc3c8a50fc75c24dffe93478753d9884; account=oauth_k1%3A6aD%2Ftm6EERwTi24qGWIzE5Q4MFsiB%2B0lezDv33CGjHbVj5CH71F2DItKxcpMmuLDEs9CH373f1ESnaqxEC81XSdYcLtP4GJUk8pq3f85YdU%3D; deviceid=08ce521ba09547bc922dd6fa2632bb7c; pub_uid=I%2B8UsO1VHCCqMM85HkyX%2Fw%3D%3D; pub_org_id=nAuEtEWLHHMw93gpyr4jNw%3D%3D; domain_org_id=103332353; dt_s=u-e5036b1-7ddc366acb-b8b22bb-74643f-641f99d2-06b061b0-a27a-431a-b4d7-534174eb948a; weiflow_token=9B5C779DC8C60AAE1AA38877985247A110193AC9667487B9CAE546934D8EFBF61448175B40A2735EC8C2712220E88FF428F5BE472EECE114BA679ED2A6DBAA0F11B72BC1EE7B3C371BD0E44C243C761BB793BCA88039BF749144B4CEAF0A419696F910986ED75C42ADC8394F77A6E477554BDA79BC474AB1DC86D385170EE7116C8497D2047CCD2F9301AEF830DE79FB091218A762095151959AC5207E05108A4C6E7440169A259F9A5D163E71634BA589CE25071E3C458710D43706042969F46F7471A3C049A23CDA74AFE311D6119348F3AD55E276B007C8ED5CBA652D81C662ACECD108D4CC271A3E6E50C952D22ADBB97078014FF8E7C9CD06DE347479C6FFA1E25D06293C54C3FB176525428E746; _csrf_token_=1640077106082; isg=BAIC_eW91xx_B8vAUb5KdLxQUwhk0wbtVeIeJEwbDXUgn6MZNGKc_XveS5vjz36F; l=eBTus1negCFwzguxBOfZlurza779AIRfguPzaNbMiOCPOBC65wy1W6dbUBTBCnGVnsspR3WAVUVyB4TEFyUBQxv9-eiD0XtZydTh.; tfstk=cCc1BENzsGj1gfvV_VTF7gXLqYPRZWb7ldZi5xeLbBopPPu1iJ5zVh8oniF4ky1..
origin: https://aflow.dingtalk.com
referer: https://aflow.dingtalk.com/dingtalk/web/query/processDesign
sec-ch-ua: "Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36
x-client-corpid: dingcc3c8a50fc75c24dffe93478753d9884
'''

forms = '''
appkey: dingcc3c8a50fc75c24dffe93478753d9884
limit: 10
title: 
processCode: PROC-010172F6-F71C-47D8-AB95-270832192EBF
processName: ?????????????????????????????????
createFrom: 2022-01-01
createTo: 2022-06-30
finishFrom: 
finishTo: 
instanceStatus: 
businessId: 
originatorUserId: 
originatorUserName: 
'''

# ???????????????????????????????????????????????????
header2 = '''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cookie: arms_uid=e9f07a1f-9cb3-4191-a6e0-0857115d1606; cna=OE8/GqCuOyUCAbfmCgVdIMdE; dd_n=CN; UM_distinctid=17dda9d3bf01c0-078824301d616-57b193e-1fa400-17dda9d3bf136d; cmouse=s35830f45-df31-461a-8369-2eef5af4171c-1640166249457; dt_org=103332353; dingtalk_corpid=dingcc3c8a50fc75c24dffe93478753d9884; account=oauth_k1%3Aejkn7xZCwhXXeOHJ9NYkvzQKhxi98scXcYgmIkUZTul67NbYKGd1ozVgUEfEPczdBs7Sho8BSvfte%2FWNNnGdMXzgVT9r7F8KfVw%2BIUWsLTU%3D; deviceid=1264afe9b5a94395bbfddf3996c99d81; pub_uid=I%2B8UsO1VHCCqMM85HkyX%2Fw%3D%3D; xlly_s=1; pub_org_id=nAuEtEWLHHMw93gpyr4jNw%3D%3D; dt_s=u-e5036b1-7de6022b51-212b3125-426fd2-70f026ae-a669b5fc-acf2-47ab-b231-d0a535a3ee4b; domain_org_id=103332353; weiflow_token=3B5C779DC8C60AAE1AA38877985247A110193AC9667487B9CAE546934D8EFBF61448175B40A2735EC8C2712220E88FF428F5BE472EECE114BA679ED2A6DBAA0F11B72BC1EE7B3C371BD0E44C243C761BB793BCA88039BF749144B4CEAF0A419696F910986ED75C42ADC8394F77A6E4775A365C2FB9F857551EE18FB312B1011194E47078527B003CB5919753D1343E15EA135CFCFCD3867606603A3C3CE42275B40E233B09B9872E1ED97A730E5CC6A12E538D23B65869683D28004152D12B28D13EA51568158F320FDAB14656C2511AD38E3E17178332DAB064C5345DB2AFA9E77413812E2B60D0089407DC7465B315115C027DFCA1F479DA0197FFD07899B1D2FA80574BF782FC69CD0D9948F06780D; _csrf_token_=1640243970750; isg=BAUFcGnOyEA5u-wZWi8lfVcRFEE_wrlU9_9GkAdqwTxLniUQzxLJJJN8qMJoxdEM; l=eBTus1negCFwzxxSBOfanurza77OSIRYYuPzaNbMiOCP_q1B50SAW6dRTxL6C3GVh6JHR35sMeeMBeYBqQAonxvTmmOrsfDmn; tfstk=cWZ5BpmZqQA7mnbe4862UOcMJCndw79sdaGuFyhw1YYqpf1DQhl1aO4H9DkKh
referer: https://aflow.dingtalk.com/dingtalk/web/query/dashboard?dinghash=aflowSetting
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
'''

header = str2header.Str2Header(headers)
data = str2header.Str2Header(forms)

last_week_start = (now - timedelta(days=9)).strftime(r'%Y-%m-%d')
last_week_end = (now - timedelta(days=3)).strftime(r'%Y-%m-%d')

# 1. ?????????????????????
# data["createFrom"] = last_week_start
# data["createTo"] = last_week_end
html = requests.post(url, headers=header, data=data)
print(html.text)

time.sleep(6)
# ????????????????????????????????????????????? jobId ??? ??????ID
# 1. ?????? jobId??????????????? form, ?????????????????? ??????ID, ??????????????????????????????????????????????????????????????????????????????
jobId = "https://aflow.dingtalk.com/dingtalk/web/query/instdata/getDataExportRecords.json"
r = requests.post(jobId, headers=header, data={'page': 1, 'limit': 10})
dic = json.loads(r.content)
jobId = dic.get('data').get('values')[0].get('jobId')
print(jobId)
time.sleep(6)

# 2. ????????????ID
header3 = '''
_csrf_token_: 1640243970750
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
client-corpid: dingcc3c8a50fc75c24dffe93478753d9884
content-length: 17
content-type: application/x-www-form-urlencoded; charset=UTF-8
cookie: arms_uid=e9f07a1f-9cb3-4191-a6e0-0857115d1606; cna=OE8/GqCuOyUCAbfmCgVdIMdE; dd_n=CN; UM_distinctid=17dda9d3bf01c0-078824301d616-57b193e-1fa400-17dda9d3bf136d; cmouse=s35830f45-df31-461a-8369-2eef5af4171c-1640166249457; dt_org=103332353; dingtalk_corpid=dingcc3c8a50fc75c24dffe93478753d9884; account=oauth_k1%3Aejkn7xZCwhXXeOHJ9NYkvzQKhxi98scXcYgmIkUZTul67NbYKGd1ozVgUEfEPczdBs7Sho8BSvfte%2FWNNnGdMXzgVT9r7F8KfVw%2BIUWsLTU%3D; deviceid=1264afe9b5a94395bbfddf3996c99d81; pub_uid=I%2B8UsO1VHCCqMM85HkyX%2Fw%3D%3D; xlly_s=1; pub_org_id=nAuEtEWLHHMw93gpyr4jNw%3D%3D; dt_s=u-e5036b1-7de6022b51-212b3125-426fd2-70f026ae-a669b5fc-acf2-47ab-b231-d0a535a3ee4b; domain_org_id=103332353; weiflow_token=3B5C779DC8C60AAE1AA38877985247A110193AC9667487B9CAE546934D8EFBF61448175B40A2735EC8C2712220E88FF428F5BE472EECE114BA679ED2A6DBAA0F11B72BC1EE7B3C371BD0E44C243C761BB793BCA88039BF749144B4CEAF0A419696F910986ED75C42ADC8394F77A6E4775A365C2FB9F857551EE18FB312B1011194E47078527B003CB5919753D1343E15EA135CFCFCD3867606603A3C3CE42275B40E233B09B9872E1ED97A730E5CC6A12E538D23B65869683D28004152D12B28D13EA51568158F320FDAB14656C2511AD38E3E17178332DAB064C5345DB2AFA9E77413812E2B60D0089407DC7465B315115C027DFCA1F479DA0197FFD07899B1D2FA80574BF782FC69CD0D9948F06780D; _csrf_token_=1640243970750; tfstk=cq0lB70kh0r7psqmfUaSMOBDybkFCFQUI2ujuV5XOyaExpLLau5mKiSalJd0Ed9PA; l=eBTus1negCFwzmtMBO5aKurza779CHOfksPzaNbMiInca1-fcGMRHNCpw1nJFdtjgt5b-etP1jLLIRnwPAzLRx6DZP67Jh2Honp68e1..; isg=BAIC1nLe1xmk7svAUb5KdLxQUwhk0wbtTF4hKUwMTHWkn4gZNGcD_XSZT5vjz36F
origin: https://aflow.dingtalk.com
referer: https://aflow.dingtalk.com/dingtalk/web/query/dashboard?dinghash=aflowSetting
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
x-client-corpid: dingcc3c8a50fc75c24dffe93478753d9884
'''
header3 = str2header.Str2Header(header3)
file_url = "https://aflow.dingtalk.com/dingtalk/web/query/instdata/getDataExportFileInfoByJobId.json"
r = requests.post(file_url, headers=header3, data={'jobId': jobId})
data_dic = json.loads(r.content)
fileid = data_dic.get('data').get('fileId')
print(fileid)

time.sleep(6)
# ??????????????????
if fileid:
    header22 = str2header.Str2Header(header2)
    geturl = 'https://aflow.dingtalk.com/dingtalk/web/instdata/filehandle?fileId=' + str(fileid) + '&corpId=dingcc3c8a50fc75c24dffe93478753d9884'
    temp = requests.get(url=geturl, headers=header22)
    with open("file.xlsx", "wb") as f:
        f.write(temp.content)
        f.close()
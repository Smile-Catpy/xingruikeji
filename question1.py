import requests
import time
import requests

kv = {
    # 定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}


def getHTMLText(url):
    """requests 爬取页面的通用代码框架 """
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        return r.text
    except Exception as err:

        return print("产生异常： ", err)


def postHTMLText(url, data):
    """requests 爬取页面的通用代码框架 """
    try:
        r = requests.post(url, data=data, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        return r.text
    except Exception as err:

        return print("产生异常： ", err)


with open("题目1.csv", "a+", encoding="utf8") as f:
    f.write("ISIN, Bond Code, Issuer, Bond Type, Issue Date, Latest Rating")
    f.write("\n")
    for a in range(1, 5):
        url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
        data = {"pageNo": "{}".format(a),
                "pageSize": "15",
                "isin": "",
                "bondCode": "",
                "issueEnty": "",
                "bondType": "100001",
                "couponType": "",
                "issueYear": "2023",
                'rtngShrt': "",
                'bondSpclPrjctVrty': ''}
        stext = postHTMLText(url=url, data=data)
        '''{"head":{"version":"2.0","provider":"CWAP","req_code":"","rep_code":"200","rep_message":"","ts":1689142103821,"producer":"","tstext":"2023-07-12 14:08:23"},"data":{"total":56,"resultList":[{"bondDefinedCode":"hhfcg30015","bondName":null,"bondCode":"230015","issueStartDate":"2023-07-14","issueEndDate":"2023-07-14","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006PJH0","inptTp":"0"},{"bondDefinedCode":"hhfcf39941","bondName":null,"bondCode":"239941","issueStartDate":"2023-07-14","issueEndDate":"2023-07-14","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006PJG2","inptTp":"0"},{"bondDefinedCode":"hhabh39940","bondName":null,"bondCode":"239940","issueStartDate":"2023-07-07","issueEndDate":"2023-07-07","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006NHK3","inptTp":"0"},{"bondDefinedCode":"hhabi39939","bondName":null,"bondCode":"239939","issueStartDate":"2023-07-05","issueEndDate":"2023-07-05","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006NHL1","inptTp":"0"},{"bondDefinedCode":"hgjjf39938","bondName":null,"bondCode":"239938","issueStartDate":"2023-07-05","issueEndDate":"2023-07-05","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006NHM9","inptTp":"0"},{"bondDefinedCode":"heihj30014","bondName":null,"bondCode":"230014","issueStartDate":"2023-06-21","issueEndDate":"2023-06-21","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006KWD3","inptTp":"0"},{"bondDefinedCode":"hfahf39937","bondName":null,"bondCode":"239937","issueStartDate":"2023-06-16","issueEndDate":"2023-06-16","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006M698","inptTp":"0"},{"bondDefinedCode":"hdhhe30013","bondName":null,"bondCode":"230013","issueStartDate":"2023-06-14","issueEndDate":"2023-06-14","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006JM06","inptTp":"0"},{"bondDefinedCode":"hdjhj39936","bondName":null,"bondCode":"239936","issueStartDate":"2023-06-09","issueEndDate":"2023-06-09","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006K5N0","inptTp":"0"},{"bondDefinedCode":"hdbda39935","bondName":null,"bondCode":"239935","issueStartDate":"2023-06-09","issueEndDate":"2023-06-09","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006JD64","inptTp":"0"},{"bondDefinedCode":"hdddg39934","bondName":null,"bondCode":"239934","issueStartDate":"2023-06-07","issueEndDate":"2023-06-07","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006JLY4","inptTp":"0"},{"bondDefinedCode":"hdddf39933","bondName":null,"bondCode":"239933","issueStartDate":"2023-06-07","issueEndDate":"2023-06-07","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006JLZ1","inptTp":"0"},{"bondDefinedCode":"hcjbh39932","bondName":null,"bondCode":"239932","issueStartDate":"2023-06-02","issueEndDate":"2023-06-02","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006JDS3","inptTp":"0"},{"bondDefinedCode":"hcdff8pp10","bondName":null,"bondCode":"239931","issueStartDate":"2023-05-26","issueEndDate":"2023-05-26","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006HB01","inptTp":"0"},{"bondDefinedCode":"hbdegy1n6f","bondName":null,"bondCode":"230012","issueStartDate":"2023-05-24","issueEndDate":"2023-05-24","bondTypeCode":"100001","bondType":"Treasury Bond","entyFullName":"Ministry of Finance of the People’s Republic of China","entyDefinedCode":"300001","debtRtng":"---","isin":"CND10006GPT1","inptTp":"0"}],"prepg":0,"pageTotal":4,"pageNo":0,"nextpg":1},"records":[]}
        '''
        import json

        strs = json.loads(stext)

        for i in strs.get("data").get("resultList"):
            # [{'bondDefinedCode': 'hhfcg30015', 'bondName': None, 'bondCode': '230015', 'issueStartDate': '2023-07-14', 'issueEndDate': '2023-07-14', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006PJH0', 'inptTp': '0'}, {'bondDefinedCode': 'hhfcf39941', 'bondName': None, 'bondCode': '239941', 'issueStartDate': '2023-07-14', 'issueEndDate': '2023-07-14', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006PJG2', 'inptTp': '0'}, {'bondDefinedCode': 'hhabh39940', 'bondName': None, 'bondCode': '239940', 'issueStartDate': '2023-07-07', 'issueEndDate': '2023-07-07', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006NHK3', 'inptTp': '0'}, {'bondDefinedCode': 'hhabi39939', 'bondName': None, 'bondCode': '239939', 'issueStartDate': '2023-07-05', 'issueEndDate': '2023-07-05', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006NHL1', 'inptTp': '0'}, {'bondDefinedCode': 'hgjjf39938', 'bondName': None, 'bondCode': '239938', 'issueStartDate': '2023-07-05', 'issueEndDate': '2023-07-05', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006NHM9', 'inptTp': '0'}, {'bondDefinedCode': 'heihj30014', 'bondName': None, 'bondCode': '230014', 'issueStartDate': '2023-06-21', 'issueEndDate': '2023-06-21', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006KWD3', 'inptTp': '0'}, {'bondDefinedCode': 'hfahf39937', 'bondName': None, 'bondCode': '239937', 'issueStartDate': '2023-06-16', 'issueEndDate': '2023-06-16', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006M698', 'inptTp': '0'}, {'bondDefinedCode': 'hdhhe30013', 'bondName': None, 'bondCode': '230013', 'issueStartDate': '2023-06-14', 'issueEndDate': '2023-06-14', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006JM06', 'inptTp': '0'}, {'bondDefinedCode': 'hdjhj39936', 'bondName': None, 'bondCode': '239936', 'issueStartDate': '2023-06-09', 'issueEndDate': '2023-06-09', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006K5N0', 'inptTp': '0'}, {'bondDefinedCode': 'hdbda39935', 'bondName': None, 'bondCode': '239935', 'issueStartDate': '2023-06-09', 'issueEndDate': '2023-06-09', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006JD64', 'inptTp': '0'}, {'bondDefinedCode': 'hdddg39934', 'bondName': None, 'bondCode': '239934', 'issueStartDate': '2023-06-07', 'issueEndDate': '2023-06-07', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006JLY4', 'inptTp': '0'}, {'bondDefinedCode': 'hdddf39933', 'bondName': None, 'bondCode': '239933', 'issueStartDate': '2023-06-07', 'issueEndDate': '2023-06-07', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006JLZ1', 'inptTp': '0'}, {'bondDefinedCode': 'hcjbh39932', 'bondName': None, 'bondCode': '239932', 'issueStartDate': '2023-06-02', 'issueEndDate': '2023-06-02', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006JDS3', 'inptTp': '0'}, {'bondDefinedCode': 'hcdff8pp10', 'bondName': None, 'bondCode': '239931', 'issueStartDate': '2023-05-26', 'issueEndDate': '2023-05-26', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006HB01', 'inptTp': '0'}, {'bondDefinedCode': 'hbdegy1n6f', 'bondName': None, 'bondCode': '230012', 'issueStartDate': '2023-05-24', 'issueEndDate': '2023-05-24', 'bondTypeCode': '100001', 'bondType': 'Treasury Bond', 'entyFullName': 'Ministry of Finance of the People’s Republic of China', 'entyDefinedCode': '300001', 'debtRtng': '---', 'isin': 'CND10006GPT1', 'inptTp': '0'}]
            isin = i.get("isin")
            f.write(isin)
            f.write(",")
            bondCode = i.get("bondCode")
            f.write(bondCode)
            f.write(",")
            Issuer = i.get("entyFullName")
            f.write(Issuer)
            f.write(",")
            bondType = i.get("bondType")
            f.write(bondType)
            f.write(",")
            IssueDate = i.get("issueStartDate")
            f.write(IssueDate)
            f.write(",")
            LatestRating = i.get("debtRtng")
            f.write(LatestRating)
            f.write(",")
            f.write("\n")

import requests
import json


def getHTML_job(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/'
                      '605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15'}
    try:
        HTML_job = requests.post(url, headers = headers)
        HTML_job.raise_for_status()
        return HTML_job.text
    except:
        return ''

def parse_json(job):
    job_json = json.loads(job)
    page_size = (job_json.get('content').get('pageSize'))
    total_page_count = job_json.get('content').get('totalPageCount')
    jobList = []
    for i in range(page_size):
        company_name = job_json.get('content').get('result')[i].get('companyShortName')
        position_name = job_json.get('content').get('result')[i].get('positionName')
        salary = job_json.get('content').get('result')[i].get('salary')
        jobList.append(company_name)
        jobList.append(position_name)
        jobList.append(salary)
    return jobList, total_page_count

def main():
    init_url = 'https://www.lagou.com/jobs/companyAjax.json?kd=python'
    company_all_list = []
    url = init_url + '&pn=' + str(1)
    job = getHTML_job(url)
    company_list,total_page_count = parse_json(job)
    company_all_list.extend(company_list)
    page_No = total_page_count
    for i in range(2, page_No+1):
        url = init_url + '&pn=' +str(i)
        job = getHTML_job(url)
        company_all_list,total_page_count = parse_json(job)
        company_all_list.extend(company_list)
        print(company_all_list)

if __name__ == '__main__':
    main()

import urllib2, json
import re 

def clean_json(json):
    return re.sub(r'new Date\(.*?\)', '""', json)

# 1.& 2. Filter to just Hillary Clinton's e-mails containing the word Benghazi
dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?searchText=Benghazi&caseNumber=F-2014-20439&page=5737&start=1&limit=114735').read()



valid_json = clean_json(dirty_json)

data = json.loads(valid_json)

# 3. printing links

for bill in data['Results']:
    print bill['pdfLink']
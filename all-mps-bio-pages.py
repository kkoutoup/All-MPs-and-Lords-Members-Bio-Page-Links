#dependencies
import urllib, re, time, datetime, csv
from requests_html import HTMLSession
from urllib.parse import urlparse

#data container
data = []

#get data function
def get_data(url):
  if url.endswith('/mps/'):
    print("=> Collecting data for House of Commons MPs")
  else:
    print("=> Collecting data for House of Lords Members")
  try:
    session = HTMLSession()
    #send request
    r = session.get(url)
    #check for errors in request
    r.raise_for_status()
  except Exception as e:
    print(e)
  else:
    #get all links from div
    all_links = r.html.find('#pnlListing', first = True).links
    #make sure links have correct structure
    hoc_pattern =  re.compile(r'https://www\.parliament\.uk/biographies/commons/(.*)/\d+')
    hol_pattern =  re.compile(r'https://www\.parliament\.uk/biographies/lords/(.*)/\d+')
    #append links to data container
    for link in all_links:
      if url.endswith('/mps/'):
        if hoc_pattern.fullmatch(link) and link not in data:
          #format name
          name = (re.match(hoc_pattern, link).group(1).replace('-', ' ')).title()+' MP'
          #tackle encoding issue for weird name characters i.e. Dr ThéRèSe  Coffey MP, óRfhlaith Begley MP etc.
          data.append(['House of Commons', urllib.parse.unquote(name, encoding='utf-8'), urllib.parse.unquote(link, encoding='utf-8')])
      else:
         if hol_pattern.fullmatch(link) and link not in data:
           #format name
           name = (re.match(hol_pattern, link).group(1).replace('-', ' ')).title()
           #append data to list
           data.append(['House of Lords', name, link])
    return data

#write to csv   
def write_to_csv(data):
  print("=> Printing to CSV")
  try:
    with open('parliament_members_data.csv', 'w') as csv_file:
      csv_writer = csv.writer(csv_file, lineterminator = '\n')
      csv_writer.writerow(['House', 'MP/Member Name', 'Biolink'])
      for item in data:
        csv_writer.writerow([item[0], item[1], item[2]])
  except Exception as e:
    print(e)
  else:
    return '=> All done!'
    
#set sequence                          
def sequence():
  start = time.time()
  hoc_links = get_data('https://www.parliament.uk/mps-lords-and-offices/mps/')
  all_links = get_data('https://www.parliament.uk/mps-lords-and-offices/lords/')  
  result = data.append(write_to_csv(all_links))
  end = time.time()
  print(f"=> All done! Process completed in(approx in min/seconds): {str(datetime.timedelta(seconds=end-start))}")

#run sequence
sequence()
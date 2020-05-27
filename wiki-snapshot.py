import siaskynet
import pyinputplus as pyip
import pathlib
from datetime import datetime
import time
import webbrowser
import wikipedia

blurb_prompt = 'Please enter the search term '
blurb_generating_snaphot = 'Generating your wikipedia snapshot for '
blurb_saved_locally = 'Your wikipedia snapshot has been saved locally as: '
blurb_current_directory = 'You will find it at the current directory: '
blurb_uploading_snapshot = 'Now uploading your wikipedia snapshot to Skynet...'
blurb_description = 'This is the Skylink that you can share with anyone to retrieve your wikipedia snapshot on any Skynet Webportal:'
blurb_url = 'Please check at the follow link: '
blurb_host = 'https://siasky.net/'

file = open('wiki_snapshot.txt', 'w', encoding='utf-8')

search_item = pyip.inputStr(prompt=blurb_prompt)
terms_list = wikipedia.search(search_item)
search_item = terms_list[0]
print(blurb_generating_snaphot + search_item)
print()

now = datetime.now()
file.write(str(now))
file.write('\n')
file.write('\n')

page = wikipedia.page(search_item)

file.write(page.title)
file.write('\n')
file.write('\n')

file.write(page.url)
file.write('\n')
file.write('\n')
file.write(page.content)
file.close()

print(blurb_saved_locally + 'wiki_snapshot.txt')
path_to_txt = pathlib.Path().absolute()
print(blurb_current_directory + str(path_to_txt))
print()
print(blurb_uploading_snapshot)
print(blurb_description)
skylink = siaskynet.Skynet.UploadFile('wiki_snapshot.txt', None)
print(skylink)
print()
url_link = blurb_host + skylink[6:]
print(blurb_url + url_link)
time.sleep(2)
webbrowser.open_new(url_link)


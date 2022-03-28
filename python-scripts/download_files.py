from cli_progress_bar import *
import requests
import os

# =====================================
# Script for file download
# Author:
#   name: limenitiz
#   email: ini.ivi@yandex.ru
# =====================================

# ===========================================================
# params
counter = 0

count_files = 100

# links = [
#     "https://test1.com/_images/0.jpg",
#     "https://test2.com/_images/0.jpg"
# ]

links = ['https://test.com/_images/'
         + str(i) + '.jpg'
         for i in range(count_files)
         ]


# ===========================================================

# Send GET request and save response as image to the output folder
# Author : https://stackoverflow.com/questions/30229231/python-save-image-from-url
def download_file(link, file_name='default_filename', filetype='.jpg'):
    if not os.path.exists('out'):
        os.mkdir('out')

    with open('out/' + file_name + str(counter) + filetype, 'wb') as handle:
        response = requests.get(link, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


print()
print('<-- Start downloading -->')
print()

for l in links:
    download_file(l, file_name='test-filename-', filetype='.jpg')
    print_progress_bar(
        counter + 1, len(links),
        prefix='Progress (' + str(counter + 1) + '/' + str(len(links)) + ') :',
        length=30)
    counter += 1

print()
print('<-- Finish downloading  --> \n')
print()

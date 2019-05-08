import requests
import json
import sys
import os

URL_PATTERN = 'https://pypi.python.org/pypi/{}/json'

package_name = sys.argv[1]

json_res = requests.get(URL_PATTERN.format(package_name)).content
data = json.loads(json_res)
print(data.keys())
last_version = data['info']['version']

print("Last version of {} is {}".format(package_name,last_version))

for download_option in data['releases'][last_version]:
    if download_option['packagetype'] == 'sdist':
        os.system("wget {}".format(download_option['url']))
        os.makedirs(package_name)
        if ".zip" in download_option['filename']:
            os.system("unzip {} -d {}".format(download_option['filename'],package_name))
            os.system("rm {}".format(download_option['filename'],package_name))
        elif ".tar" in download_option['filename']:
            os.system("tar -C  {} -xvf {}".format(package_name,download_option['filename']))
            os.system("rm {}".format(download_option['filename'],package_name))


import requests
import json
import sys
import os

URL_PATTERN = 'https://pypi.python.org/pypi/{}/json'

if len(sys.argv) == 2:
    package_name = sys.argv[1]
    version = "latest"
elif len(sys.argv) == 3:
    package_name = sys.argv[1]
    version = sys.argv[2]

json_res = requests.get(URL_PATTERN.format(package_name)).content.decode()

if "none-any" in json_res:
    print("No need to compile!")
    sys.exit(0)

data = json.loads(json_res)
print(data.keys())

if version == 'latest':
    last_version = data['info']['version']
else:
    last_version = version

print("Last version of {} is {}".format(package_name,last_version))

for download_option in data['releases'][last_version]:
    if download_option['packagetype'] == 'sdist':
        os.system("wget {}".format(download_option['url']))
        os.makedirs(package_name)
        if ".zip" in download_option['filename']:
            os.system("unzip {} -d {} 1>/dev/null".format(download_option['filename'],package_name))
            os.system("rm {}".format(download_option['filename'],package_name))
        elif ".tar" in download_option['filename']:
            os.system("tar -C  {} -xvf {} 1>/dev/null".format(package_name,download_option['filename']))
            os.system("rm {}".format(download_option['filename'],package_name))


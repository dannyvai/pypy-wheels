import os
import sys
import subprocess
import shutil
import glob

git_packages = open("packages.lst","r").readlines()

def is_package_built(package_name):
    built_packages = os.listdir("/root/wheels/")
    for pkg_name in built_packages:
        if package_name in pkg_name:
            return True
    return False

for package in git_packages:

    package=package.strip()
    if " " in package:
        package,version = package.split(" ")
    else:
        version = None

    if is_package_built(package):
        continue

    print("Downloading {}".format(package))
    if not os.path.exists(package):
        if version is None:
            proc = subprocess.Popen(["python", "download_package.py", "{}".format(package)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        else:
            proc = subprocess.Popen(["python", "download_package.py", package,version],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

        ret =  proc.communicate()[0].decode()
        #print(ret)
        if "No need to compile!" in ret:
            print("No need to compile!")
            continue

        if "error" in str(ret.lower()):
             print("Error downloading ",package)
             print(ret)
             #print(ret)

    print("Building wheel {}".format(package))
    proc = subprocess.Popen(["find", ".", "-name",'setup.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    ret =  proc.communicate()[0].decode()
    if len(ret.strip()) > 0:
        for line in ret.split('\n'):
            if package in line:
                cur_dir = os.getcwd()

                setup_py_dir = os.sep.join(line.split(os.sep)[:3])
                print("setup.py is here: {}".format(setup_py_dir))
                os.chdir(setup_py_dir)
                print("Changed dir to {}".format(os.getcwd()))
                print("Compiling for pypy2.7")
                os.system('/bin/bash -c "source ~/pypy2_venv/bin/activate; python setup.py bdist_wheel"')
                #proc = subprocess.Popen(["/home/dwainshtein/pypy2.7-v7.1.1-linux64/bin/pypy", "setup.py", "bdist_wheel"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                #ret =  proc.communicate()[0]
                #print(ret)

                print("Installing for pypy2.7")
                whl_files = glob.glob("./dist/*.whl")
                if len(whl_files) == 0:
                    print("Error building wheel for {} for pypy2.7".format(package))
                else:
                    os.system('/bin/bash -c "source ~/pypy2_venv/bin/activate; pip install {}"'.format(whl_files[0]))

                print("Copy wheels")
                os.system("mv ./dist/*.whl ~/wheels/")


                print("Compiling for pypy3.6")
                os.system('/bin/bash -c "source ~/pypy3_venv/bin/activate; python setup.py bdist_wheel"')
                #proc = subprocess.Popen(["python", "setup.py", "bdist_wheel"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                #ret =  proc.communicate()[0].decode()
                #print(ret)

                print("Installing for pypy3.6")
                whl_files = glob.glob("./dist/*.whl")
                if len(whl_files) == 0:
                    print("Error building wheel for {} for pypy3.6".format(package))
                else:
                    os.system('/bin/bash -c "source ~/pypy3_venv/bin/activate; pip install {}"'.format(whl_files[0]))
                    #proc = subprocess.Popen(["pip", "install", whl_files[0]],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    #ret =  proc.communicate()[0].decode()
                    #print(ret)

                print("Copy wheels")
                os.system("mv ./dist/*.whl ~/wheels/")
 
                os.chdir(cur_dir)
                shutil.rmtree(package)               
                break

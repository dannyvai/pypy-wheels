sudo apt-get install -y wget
sudo apt-get install -y gcc g++ make

sudo apt-get install -y libssl-dev
sudo apt-get install -y libxml2-dev libxslt-dev cython # lxml
sudo apt-get install -y libpq-dev # psycopg2
sudo apt-get install -y libjpeg-dev # pillow
sudo apt-get install -y libcurl4-openssl-dev # pycurl
sudo apt-get install -y libcups2-dev # pycups
sudo apt-get install -y libpng-dev libfreetype6-dev # matplotlib
sudo apt-get install -y swig # M2crypto
sudo apt-get install -y libsasl2-dev  libldap2-dev # python-ldap
sudo apt-get install -y libgeos-dev # Shapely
sudo apt-get install -y libmemcached-dev # pylibmc
sudo apt-get install -y libmysqlclient-dev # tiddlywebplugins.tiddlyspace
sudo apt-get install -y freetds-dev # pymssql
sudo apt-get install -y hdf5-tools libhdf5-dev # h5py
sudo apt-get install -y libblas-dev liblapack-dev gfortran # numpy
sudo apt-get install -y locales apt-utils ncurses-term
sudo apt-get install -y libfreetype6-dev
sudo apt-get install -y pkg-config
sudo apt-get install -y git
wget https://bitbucket.org/pypy/pypy/downloads/pypy2.7-v7.1.1-linux64.tar.bz2
wget https://bitbucket.org/pypy/pypy/downloads/pypy3.6-v7.1.1-linux64.tar.bz2
tar -xvf pypy2.7*.tar.bz2
tar -xvf pypy3.6*.tar.bz2
bash config_pypy.sh pypy2.7*/bin/pypy
bash config_pypy.sh pypy3.6*/bin/pypy3

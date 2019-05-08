PYPY_PATH=$1

$PYPY_PATH -m ensurepip
$PYPY_PATH -mpip install --upgrade pip setuptools
$PYPY_PATH -mpip install wheel 
$PYPY_PATH -mpip install cython

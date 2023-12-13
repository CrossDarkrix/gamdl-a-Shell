import os
import urllib.request
import ssl
import subprocess
import sys
import time
import re
from pip._internal.cli.main import main as pip

try:
    ssl._create_default_https_context = ssl._create_unverified_context
except:
    pass
if not os.path.exists('gamdl_work'):
    os.makedirs('gamdl_work', exist_ok=True)
os.chdir('gamdl_work')
print('Installing Chardet.......')
pip(['install', '--upgrade', 'chardet'])
if not os.path.exists('PyYAML-6.0.1-py3-none-any.whl'):
    with open('PyYAML-6.0.1-py3-none-any.whl', 'wb') as yaml:
        yaml.write(urllib.request.urlopen('https://raw.githubusercontent.com/CrossDarkrix/gamdl-a-Shell/main/PyYAML-6.0.1-py3-none-any.whl').read())
print('Installing PyYaml.......')
# subprocess.run('pip install PyYAML-6.0.1-py3-none-any.whl', shell=True, stdout=subprocess.PIPE)
pip(['install', '--upgrade', 'PyYAML-6.0.1-py3-none-any.whl'])
if not os.path.exists('gamdl-1.9.10.3-py3-none-any.whl'):
    with open('gamdl-1.9.10.3-py3-none-any.whl', 'wb') as gamdl:
        gamdl.write(urllib.request.urlopen('https://raw.githubusercontent.com/CrossDarkrix/gamdl-a-Shell/main/gamdl-1.9.10.3-py3-none-any.whl').read())
print('Installing gamdl Without Music Video DL Edition.......')
# subprocess.run('pip install gamdl-1.9.10.3-py3-none-any.whl', shell=True, stdout=subprocess.PIPE)
pip(['install', '--upgrade', 'gamdl-1.9.10.3-py3-none-any.whl'])
print('Setting gamdl.............')
install_path = re.search('/var/mobile/Containers.+', '\n'.join(sys.path)).group()
os.chdir(install_path)
time.sleep(1.5)
try:
    os.rename(os.path.join(install_path, 'Crypto'), os.path.join(install_path, 'Crypto.old')) # use builtin module
except:
    pass
try:
    os.rename(os.path.join(install_path, 'Cryptodome'), os.path.join(install_path, 'Cryptodome.old'))
except:
    pass
os.chdir(os.path.join(os.getenv('HOME'), 'Documents'))
print('Setting Done!\n Enjoy!')

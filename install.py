import os
import urllib.request
import ssl
import subprocess
import sys
import re

try:
    ssl._create_default_https_context = ssl._create_unverified_context
except:
    pass
if not os.path.exists('gamdl_work'):
    os.makedirs('gamdl_work', exist_ok=True)
os.chdir('gamdl_work')

if not os.path.exists('PyYAML-6.0.1-py3-none-any.whl'):
    with open('PyYAML-6.0.1-py3-none-any.whl', 'wb') as yaml:
        yaml.write(urllib.request.urlopen('https://raw.githubusercontent.com/CrossDarkrix/gamdl-a-Shell/main/PyYAML-6.0.1-py3-none-any.whl').read())
print('Installing PyYaml.......')
subprocess.run('python -m pip install PyYAML-6.0.1-py3-none-any.whl', shell=True, stdout=subprocess.PIPE)
if not os.path.exists('gamdl-1.9.10.3-py3-none-any.whl'):
    with open('gamdl-1.9.10.3-py3-none-any.whl', 'wb') as gamdl:
        gamdl.write(urllib.request.urlopen('https://raw.githubusercontent.com/CrossDarkrix/gamdl-a-Shell/main/gamdl-1.9.10.3-py3-none-any.whl').read())
print('Installing Without Music Video DL Edition.......')
subprocess.run('python -m pip install gamdl-1.9.10.3-py3-none-any.whl', shell=True, stdout=subprocess.PIPE)
print('Setting gamdl.............')
install_path = re.search('/var/mobile/Containers.+', '\n'.join(sys.path)).group()
os.chdir(install_path)

if os.path.exists('Crypto'):
    print('Crypto Module to Crypto.old: use builtin module')
    try:
        os.rename('Crypto', 'Crypto.old') # use builtin module
    except:
        pass
if os.path.exists('Cryptodome'): # use builtin module
    print('Cryptodome Module to Cryptodome.old: use builtin module')
    try:
        os.rename('Cryptodome', 'Cryptodome.old')
    except:
        pass
os.chdir(os.path.join(os.getenv('HOME'), 'Documents'))
print('Setting Done!\n Enjoy!')

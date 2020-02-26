import os
import shutil

APP_NAME = 'AutomatorMaker'
datas = {}


def add_data(src, dest):
    if os.path.exists(src):
        datas[src] = dest


# reset dist directory.
shutil.rmtree('./build', ignore_errors=True)
shutil.rmtree('./dist', ignore_errors=True)

add_data('./app/res/libs/adb', './app/res/libs')

data_str = ''
for k, v in datas.items():
    data_str += ' \\\n\t'
    data_str += '--add-data "%s:%s"' % (k, v)

pyi_cmd = 'pyinstaller -F -w -n "%s" %s \\\n__main__.py' % (APP_NAME, data_str)
print(pyi_cmd)
os.system(pyi_cmd)
os.unlink('./%s.spec' % APP_NAME)
shutil.rmtree('./build', ignore_errors=True)
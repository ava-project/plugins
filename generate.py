import os
import zipfile

files = os.listdir(".")

def create_plugin(f):
    with zipfile.ZipFile('{}.zip'.format(f), 'w') as plugin:
        files_plugin = os.listdir(f)
        for file_plugin in files_plugin:
            plugin.write('{}/{}'.format(f, file_plugin))

for f in files:
    if not os.path.isdir(f):
        continue
    manifest = '{}/manifest.json'.format(f)
    if not os.path.exists(manifest):
        continue
    create_plugin(f)

print('№1')

import os

root_folder = 'my_project'
folders_2 = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(root_folder):
    for folders_2 in folders_2:
        os.makedirs(os.path.join(root_folder, folders_2))
    print('... Starter created successfully')
else:
    print(f'{root_folder} already exist')

print('№4')
import os

all_files = []
for root, dirs, files in os.walk('../'):
    for file in files:
        all_files.append(os.path.getsize(os.path.join(root, file)))
max_size = max(all_files)

my_dict = {}
i = 1
for x in range(len(str(max_size))):
    i *= 10
    if i == 10:
        my_dict[int(i)] = len([file for file in all_files if i >= file >= 0])
    else:
        my_dict[int(i)] = len([file for file in all_files if i >= file >= i / 10])
print(my_dict)

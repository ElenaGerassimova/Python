print('#1')
with open('e84f9ad49c706008fba3b58e2a1e5b09.txt', 'r', encoding='utf8') as f:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6])for line in f)
    for i in content:
        print(i)
f.close()

print('#3')
from itertools import zip_longest
dict = {}
with open('user.txt', encoding='utf-8') as users:
    with open('hobby.txt', encoding='utf-8') as hobby:
        num_lines_users = sum(1 for line in users)
        num_lines_hobby = sum(1 for line in hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for line_user, line_user_hobby in zip_longest(users, hobby):
            dict[line_user.strip()] = line_user_hobby.strip() if \
                line_user_hobby is not None else line_user_hobby

print(dict)


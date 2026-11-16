# Reported style question: detect duplicate emails (like LeetCode #929)
from collections import defaultdict


def normalize(email):
    local, sep, domain = email.strip().lower().partition('@')
    if not local or not sep or not domain:
        raise ValueError(f'invalid email: {email}')
    # ignore everything after '+' and all dots in the local part
    local = local.split('+')[0].replace('.', '')
    return f'{local}@{domain}'


def find_duplicates(emails):
    groups = defaultdict(list)
    for e in emails:
        groups[normalize(e)].append(e)
    return {k: v for k, v in groups.items() if len(v) > 1}


if __name__ == '__main__':
    print(find_duplicates(['a.b+x@gmail.com', 'ab@gmail.com', 'AB@Gmail.com', 'c@x.com']))
    print(find_duplicates(['one@x.com', 'two@x.com']))  # {}
    try:
        normalize('not-an-email')
    except ValueError as err:
        print('error handled:', err)

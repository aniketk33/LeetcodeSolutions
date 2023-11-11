from typing import List


def unique_emails(emails: List[str]):
    # to store the unique emails
    result = set()

    for email in emails:
        local_name, domain_name = email.split('@')
        # process the local_name with the given rules
        if '+' in local_name:
            local_name = local_name.split('+')[0]
        if '.' in local_name:
            local_name = local_name.replace('.', '')
        # add the processed local and domain name to the result set
        result.add((local_name, domain_name))

    return len(result)


email_arr = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
res = unique_emails(email_arr)
print(res)

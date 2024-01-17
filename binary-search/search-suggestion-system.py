def search(products, search_word):
    result = []
    products.sort()

    word = ''
    for s in search_word:
        word += s
        curr_search = []
        for product in products:
            if not product.startswith(word) or len(curr_search) >= 3:
                continue
            curr_search.append(product)

        result.append(curr_search)

    return result


# better solution using two pointers
def search_2(products, search_word):
    result = []
    products.sort()

    left_ptr, right_ptr = 0, len(products) - 1
    for i in range(len(search_word)):
        s = search_word[i]

        # check if the pointers are in range and move the pointers if they do not match
        while left_ptr <= right_ptr and (len(products[left_ptr]) <= i or products[left_ptr][i] != s):
            left_ptr += 1
        while left_ptr <= right_ptr and (len(products[right_ptr]) <= i or products[right_ptr][i] != s):
            right_ptr -= 1

        remaining_items = left_ptr + right_ptr + 1
        result.append([])
        for j in range(min(remaining_items, 3)):
            result[-1].append(products[left_ptr + j])

    return result


res = search(["mobile", "mouse", "moneypot", "monitor", "mousepad"], 'mouse')
print(res)

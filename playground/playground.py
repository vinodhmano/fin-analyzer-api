categories = {
    'GAS': ['GAS'],
    'GROCERIES' : ['COSTCO', 'CASH & CARRY'],
    'RESTAURANT': ['Paradise Biryani'],
    'HOME_IMPROVEMENT': ['LOWES']
}

desc = 'MIRAMAR CASH & CARRY SAN'

for c, key_words in categories.items():
    for word in key_words:
        if word.lower() in desc.lower():
            print(c.lower())

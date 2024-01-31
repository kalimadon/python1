def test_format_data_for_excel(data):
    result = 'given,family,title\n'
    for person in data:
        result += person["given_name"]+','
        result += person["family_name"] +','
        result += person["title"] + '\n'
    return result
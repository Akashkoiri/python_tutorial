Name_list = ['Receive', 'the', 'following', 'device', 'for', 'estimate', '/', 'repair', 'from','the', 'Mr.', 'Akash', 'koiri']
i = 0
while Name_list[i] != 'Mr.':
    Name_list.remove(Name_list[i])
    i += 1
    break
print(Name_list)
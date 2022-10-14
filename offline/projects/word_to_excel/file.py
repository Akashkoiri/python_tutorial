import docx
doc = docx.Document("CPR job sheet 2.docx")


Name_list = ''
Name = ''
Number = ''
Email = ''

for table in doc.tables:
    for row in table.rows:
        for i in range(len(row.cells)):
            if 'Mr.' in row.cells[i].text and 'Mr.' not in Name_list:
                Name_list = row.cells[i].text.split()
              
                # for j in Name_list:
                #     if j != 'Mr.':
                #         Name_list.remove(j)
                #     break
                
                


            if row.cells[i].text == 'Mobile No.':
                if row.cells[i+1].text not in Number:
                    Number = row.cells[i+1].text

            if row.cells[i].text == 'E-mail':
                if row.cells[i+1].text not in Email:
                    Email = row.cells[i+1].text
            


print(Name_list)
print(Number)
print(Email)
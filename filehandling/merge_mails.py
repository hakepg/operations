from os import name

with open('C:\\Users\\Pratima Hake\\Desktop\\name.txt','r') as name_file:


    with open('C:\\Users\\Pratima Hake\\Desktop\\body.txt','r') as body_file:
        body=body_file.read()

        for line in name_file:
            mail="Hello" + name + body

            with open(name.strip() +' .txt','w') as mail_file:
                mail_file.write(mail)






first_list = []
second_list = ['Hello', 3.14, 17, 'Python', 87]

first_list.append(second_list[2])
first_list.append(second_list[4])

print(first_list)


email = 'aSsldjgh;OJ'

def mail_date(email):
    email = email.lower()
    email = email.capitalize()
    return email

print(mail_date(email))



q = 0
q1 = 0
a = int(input())
while a != 0:
    q += 1
    if a % 3 == 0 and a % 2 != 0:
        q1 += 1
        a = int(input())
print(q)
print(q1)








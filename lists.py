some_num = 4  # integer (whole number)
some_decimal = 3.14  # float (decimal number)
some_str = "Hello, SmartNinja!"  # string
human = True  # boolean (either True or False)

number_list = [34, 1, 2, 3, 4, 5, 64, 78, 99, 169]
string_list = ["word 1", "word 2", "the first sentence"]
person = ["Sepp", "Huber", 28, "männlich", 8010, "Graz"]

summe = 0

for i in number_list:
    summe += i

print(summe)

number_list.sort()

for element in number_list:
    print(element)

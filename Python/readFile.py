# Program to read the entire file using read() function
file = open("d:/OneDrive/studies/Bar-Ilan/pyton/BI-Python/text_file.txt", "r", encoding='UTF8')
content = file.read()
print(content)
file.close()

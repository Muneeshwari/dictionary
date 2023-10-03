no=int(input("Enter no of subject:"))
for i in range(no):
    subject=input('Enter your subject:')
    mark=int(input('Enter your mark:'))
    mark_dictionary={subject,mark}
    print(mark_dictionary)
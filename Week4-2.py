s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
studentName= input('Enter student\'s name')
if studentName=='Ahmad':
    sum=s1[1]+s1[2]+s1[3]+s1[4]+s1[5]
    print(s1[0]+' '+str(sum))
elif studentName=='Sami':
    sum=s2[1]+s2[2]+s2[3]+s2[4]+s2[5]
    print(s2[0]+' '+str(sum))
elif studentName=='Faris':
    sum=s3[1]+s3[2]+s3[3]+s3[4]+s3[5]
    print(s3[0]+' '+str(sum))
else:
    print('Student is not recorded 0')

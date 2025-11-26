import string
source="12345"


source_words=source.split()
print(source_words)


typed="12345"
typed_words=typed.split()
print(typed_words)
#有一个准确度
correctness=0
#准确度除以输入的长度->正确度


for i in range(min(len(typed_words),len(source_words))):
    if typed_words[i]==source_words[i]:
        correctness+=1
        

print(correctness)#9
print((correctness/len(typed_words))* 100)

print()
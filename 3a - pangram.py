def abc(str1,alphabet=string.ascii_lowercase):
alphaset=set(alphabet)
return alphaset<=set(str1.lower())
print(abc('The quick brown fox jumps over the lazy dog'))
print(abc('Hello'))

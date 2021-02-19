text = "X-DSPAM-Confidence:    0.8475"
p=text.find(':')
newstr= text[p+1:]
p=newstr.lstrip(" ")
print(float(p))

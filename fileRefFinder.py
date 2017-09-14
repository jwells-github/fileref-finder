import pyperclip, re

matchesFromClipboard = []
matchesShortened = []
matchesSort = []
matchOutput = []

#CREATE FILE REFERENCE  REGEX

fileRefRegex = re.compile(r'''(
    (\d{4})                 #First four numbers of reference
    (CNA|cna|CNS|cns|
     KRS|krs|VNA|vna|
     VNS|vns|ICC|icc|       #FileRef
     BDS|bds|NOV|nov|
     BCT|bct|CTC|ctc|
     HTC|htc|BDA|bda) 
    (\d{3})                 # Last 3 digits 
    (A|B|C)?                # Sometimes file references that are duplicated end in an A/B/C
    )''', re.VERBOSE)


#LOCATE MATCHES IN CLIPBOARD TEXT

clipboardText = str(pyperclip.paste())

for groups in fileRefRegex.findall(clipboardText):
    fileRef = ''.join([groups[0]])
    matchesFromClipboard.append(fileRef)
    

#SORT FILE REFERENCES BY LAST 3 DIGITS
    
for i in matchesFromClipboard:
    t=i
    t=t[7:11]
    matchesShortened.append(t)

matchesShortened.sort()



for i in matchesFromClipboard:
    c = 0
    length = len(matchesFromClipboard)
    while c < length:
        if i[7:11] == matchesShortened[c]:
            cNumber = str(c)
            matchesSort.append(cNumber+ ' ' +i)
            c=0
            break
        else:
            c+=1
matchesSort.sort()

for i in matchesSort:
    t=i
    t=i[2:15]
    matchOutput.append(t)

#COPY MATCHES TO THE CLIPBOARD
    
if len(matchesFromClipboard) > 0:
    pyperclip.copy('\n'.join(matchOutput))
    print('Copied to clipboard:')

else:
    print('No filereferences found')

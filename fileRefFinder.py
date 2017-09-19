import pyperclip, re

matchesFromClipboard = []
matchesShortened = []
matchesSort = []
matchOutput = []

#FILE REFERENCE  REGEX

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

#Searches the clipboard text for file references and appends them to the matchesFromClipboard list
for groups in fileRefRegex.findall(clipboardText):
    fileRef = ''.join([groups[0]])
    matchesFromClipboard.append(fileRef)
    

#SORT FILE REFERENCES BY LAST 3 DIGITS

#Appends the last 3 digits of every file reference to the matchesShortened List    
for i in matchesFromClipboard:
    t=i
    t=t[7:11]
    matchesShortened.append(t)

matchesShortened.sort()

for i in matchesFromClipboard:
    c = 0
    length = len(matchesFromClipboard)
    #Compares the full file reference to the sorted, shortened file reference
    #Appends the list position of the shortened file reference to the beginning of the full file reference
    while c < length:
        if i[7:11] == matchesShortened[c]:
            cNumber = str(c)
            matchesSort.append(cNumber+ ' ' +i)
            c=0
            break
        else:
            c+=1
#Sorts the full file refernce list by the appended list position number
matchesSort.sort()

#Removes the appended list position number from the start of the full file reference
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

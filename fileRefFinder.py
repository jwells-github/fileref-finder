import pyperclip, re

#CREATE FILE REFERENCE  REGEX

fileRefRegex = re.compile(r'''(
    (\d{4})                 #First four numbers of reference
    (CNA|cna|CNS|cns|
     KRS|krs|VNA|vna|
     VNS|vns|ICC|icc|       #FileRef
     BDS|bds|NOV|nov|
     BCT|bct|CTC|ctc|
     HTC|htc) 
    (\d{3})                 # Last 3 digits 
    (A|B|C)?                # Sometimes file references that are duplicated end in an A/B/C
    )''', re.VERBOSE)


#LOCATE MATCHES IN CLIPBOARD TEXT

matches = []

clipboardText = str(pyperclip.paste())

for groups in fileRefRegex.findall(clipboardText):
    fileRef = ''.join([groups[0]])
    matches.append(fileRef)

#SORT FILE REFERENCES BY LAST 3 DIGITS



#COPY MATCHES TO THE CLIPBOARD
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')

else:
    print('No filereferences found')

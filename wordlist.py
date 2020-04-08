import subprocess as sp

word = input("[*] Enter word : ")
length = int(input("[*] Input the length : "))

file = open(word + '.txt', "w")
file.close() 

totalLength = len(word) + length
padding = 0
file = ['cat']

for i in range(length):
    pattern = word + '@' * (length - padding)
    fileOutput = word + str(padding) + '.txt'
    cmd = ['crunch',str(totalLength-padding),str(totalLength-padding),'1234567890','-t',pattern,'-o',fileOutput]
    padding = padding + 1
    file.append(fileOutput)    
    sp.call(cmd)
                                
file.extend(['>',word + '.txt'])
sp.call(file)

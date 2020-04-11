import subprocess as sp
import os


#This script using crunch https://github.com/crunchsec/crunch

welcome = """                    
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║       ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║       ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║       ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
By Mekel Ilyasa
github.com/retr00exe
"""
print(welcome)

wordList = input("[*] Enter list of word : ").split()
length = int(input("[*] Enter the number of digits : "))
print()
file = ['cat']

for word in wordList:
    padding = 0
    totalLength = len(word) + length
    for i in range(length):
        pattern = word + '@' * (length - padding)
        fileOutput = word + str(padding) + '.txt'
        cmd = ['crunch',str(totalLength-padding),str(totalLength-padding),'1234567890','-t',pattern,'-o',fileOutput]
        padding = padding + 1
        file.append(fileOutput)    
        sp.call(cmd)
    
file.extend(['>',word + '.txt'])
print("FINISHED!)

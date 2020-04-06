import os
import pypandoc
import sys

'''
Converts all files in current directory from one type to another

Usage: 
`$ python conv-doc <Input File Type> <Output File Type>`

Example Use:
python conv-doc docx md

Allowable Formats:
https://pandoc.org/

'''


inType = sys.argv[1]
outType = sys.argv[2]


headerStr = f"Converting {inType} into {outType}"
print("\n","-"*len(headerStr),"\n",headerStr,"\n","-"*len(headerStr),"\n",sep='')

fileDir = r'.'

for filename in os.listdir(fileDir):
   extension = filename[(-1*len(inType)):]
   name = filename[:(-1*(len(inType)+1))]
   if extension == inType:
      print(f"* Converting: {filename} --> {name}"+"."+outType)
      output = pypandoc.convert_file(str(fileDir + '/' + filename), outType, outputfile=(fileDir + '/' +  name+'.'+outType))
      assert output == ""

print("")
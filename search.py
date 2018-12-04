import PyPDF2
import sys
import re

if len(sys.argv) != 3:
    print("Command Usage: python3 search.py <xyz.pdf> <pattern>")
    sys.exit()

param=sys.argv[1]
#print(param)
# open the pdf file
object = PyPDF2.PdfFileReader(param)
if object.isEncrypted:
    print('PDF is encrypted. Cannot Proceed further')
    sys.exit()

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = sys.argv[2]

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    #print("this is page " + str(i))
    Text = PageObj.extractText()
    #print(Text)
    if re.search(String, Text):
        print('Found Match on page '+str(i+1))

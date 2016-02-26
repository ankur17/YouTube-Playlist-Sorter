#import os
#from bs4 import BeautifulSoup
#
#def Print(l):
#	for _ in l:
#		print _
#soup = BeautifulSoup(open('file.html','r'))
#ols = list()
#uls = list()
#s = set()
#'''
#han = open('list.txt','w')
#han.write('')
#han.close()
#
#
#han = open('list.txt','a')
#
#oo=''
#for link in soup.find_all('tr'):
#    oo = link.get('data-title')
#    han.write(oo+'.mp4\n')
#    ols.append(oo)
#han.close()
#'''
#han = open('list.txt','r')
#for a in han:
#	ols.append(a.rstrip())
#
#han.close()
#ulst = os.listdir('./folder')
#Print(ulst)
#print"-----------"
#Print(ols)
##print ulst
##for a in ols:
##	if a not in uls:
##		s.add(a)
##print s
#p = './folder'
#faulty_words = list()
#index = -22
#for a in ols:
#	index = ols.index(a)
#	new_word = str(index+1) + ' ' + a
#	try:
#		os.rename(os.path.join(p,a),os.path.join(p,new_word))
#	except Exception, e:
#		faulty_words.append(a)
#		pass
#	#print new_word
#	#os.rename(p+"\\"+os.listdir(p)[1],p+"\\""ola.txt")
#print "Following are the list of the words that could not be renamed:"
#for a in faulty_words:
#	print a

'''PROGRAM TO RENAME THE UNORDERED DOWNLOADED YOUTUBE PLAYLIST FILES ACCORDING TO THE SEQUENCE OF THE PLAYLIST'''
import os
import urllib2
from bs4 import BeautifulSoup
url = raw_input("Enter the youtube plalist Url: ")
def Print(l):
	for _ in l:
		print _
soup = BeautifulSoup(urllib2.urlopen(url))
ols = list()
uls = list()
s = set()


oo=''
for link in soup.find_all('tr'):
    oo = link.get('data-title')
    ols.append(oo+'.mp4')



ulst = os.listdir('./folder')

#print ulst
#for a in ols:
#	if a not in uls:
#		s.add(a)
#print s
p = './folder'
faulty_words = list()
index = -22
for a in ols:
	index = ols.index(a)
	new_word = str(index+1) + ' ' + a
	try:
		os.rename(os.path.join(p,a),os.path.join(p,new_word))
	except Exception, e:
		faulty_words.append(a)
		pass
	#print new_word
	#os.rename(p+"\\"+os.listdir(p)[1],p+"\\""ola.txt")
if len(faulty_words):
	print "Following are the list of the words that could not be renamed:"
	Print(faulty_words)
print "Done"
print len(ols),"File(s) Renamed"
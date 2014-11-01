import urllib2
from collections import Counter

def get_piece_names():
    nameslist=[]
    for i in xrange(0,368): #367 total pages
        rohurl="http://www.rohcollections.org.uk/SearchResults.aspx?searchtype=performance&company=The%20Royal%20Ballet&genre=Ballet&page="+str(i)
        results=urllib2.urlopen(rohurl)
        for l in results.readlines():
            try:
                if l.count('<td>')>0 and l.count('<a href')==0 and l.count('<td>The Royal Ballet</td>')==0 and l.count('<td>Matinee</td>')==0 and l.count('<td>Evening</td>')==0:
                    corename=l.split('<td>')[-1].split('</td>')[0]
                    nameslist.append(corename)
            except UnicodeDecodeError:
                print "Ignoring UnicodeDecodeError"
        print("Page " + str(i+1) + " parsed!")
        results.close()
    print(Counter(nameslist))
    nameset=set(nameslist)
    nameslist=list(nameset)
    nameslist.sort()
    return nameslist

def printpiecenamestofile(path_to_filename):
    piece_list=get_piece_names()
    myfile=open(path_to_filename,'w')
    for pname in piece_list:
        myfile.write(pname+'\n')
    myfile.close

#printchoreonamestofile('./piecenames.txt')

print get_piece_names()

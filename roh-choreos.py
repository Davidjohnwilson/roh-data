import urllib2
from collections import Counter

def get_choreo_names():
    nameslist=[]
    for i in xrange(0,20):
        rohurl="http://www.rohcollections.org.uk/SearchResults.aspx?searchtype=work&company=The%20Royal%20Ballet&genre=Ballet&page="+str(i)
        results=urllib2.urlopen(rohurl)
        for l in results.readlines():
            try:
                if l.count('(')>0 and l.count(')')>0:
                    splitl=l.split('(')
                    first_piece=splitl[-1].split(')')
                    name=first_piece[0]
                    if name.count('./')>0:
                        name="" #do nothing
                    elif name[0].islower():
                        name=""
                    elif name.count(',')>0:
                        names=name.split(',')
                        for n in names:
                            if n[0]==' ':
                                n=n[1:]
                            nameslist.append(n)
                    else:
                        if name[0]==' ':
                            name=name[1:]
                        nameslist.append(name)
            except UnicodeDecodeError:
                print "Ignoring UnicodeDecodeError"
        results.close()
    print(Counter(nameslist))
    nameset=set(nameslist)
    nameslist=list(nameset)
    nameslist.sort()
    return nameslist

def printchoreonamestofile(path_to_filename):
    choreolist=get_choreo_names()
    myfile=open(path_to_filename,'w')
    for cname in choreolist:
        myfile.write(cname+'\n')
    myfile.close

#printchoreonamestofile('/Users/davidwilson/Desktop/choreonames.txt')

print get_choreo_names()

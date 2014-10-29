import urllib2
from collections import Counter

def get_piece_dates():
    dateslist=[]
    for i in xrange(0,368): #367 total pages
        rohurl="http://www.rohcollections.org.uk/SearchResults.aspx?searchtype=performance&company=The%20Royal%20Ballet&genre=Ballet&page="+str(i)
        results=urllib2.urlopen(rohurl)
        for l in results.readlines():
            try:
                if l.count('<td>')>0 and l.count("<a href='performance.")>0 and l.count('<td>The Royal Ballet</td>')==0 and l.count('<td>Matinee</td>')==0 and l.count('<td>Evening</td>')==0:
                    date=l.split("page="+str(i)+"'>")[-1].split('</a>')[0]
                    dateslist.append(date)
            except UnicodeDecodeError:
                print "Ignoring UnicodeDecodeError"
        print("Page " + str(i+1) + " parsed!")
        results.close()
    print(Counter(dateslist))
    # datesset=set(dateslist)
    # dateslist=list(datesset)
    # dateslist.sort()
    return dateslist

def get_piece_years(dateslist):
    yearslist = [x.split(" ")[-1] for x in dateslist]
    print(Counter(yearslist))
    yearsset = set(yearslist)
    yearslist = list(yearsset)
    yearslist.sort()
    return yearslist

def get_piece_months(dateslist):
    monthslist = [x.split(" ")[1] for x in dateslist]
    print(Counter(monthslist))
    monthsset = set(monthslist)
    monthslist = list(monthsset)
    monthslist.sort()
    return monthslist

def printpiecenamestofile(path_to_filename):
    piece_list=get_piece_years()
    myfile=open(path_to_filename,'w')
    for pname in piece_list:
        myfile.write(pname+'\n')
    myfile.close

#printchoreonamestofile('./piecenames.txt')
dateslist = get_piece_dates()
print(get_piece_years(dateslist))
print(get_piece_months(dateslist))


def get_piece_times():
    timeslist=[0,0] #matinee=0, evening=1 
    for i in xrange(0,368): #367 total pages
        rohurl="http://www.rohcollections.org.uk/SearchResults.aspx?searchtype=performance&company=The%20Royal%20Ballet&genre=Ballet&page="+str(i)
        results=urllib2.urlopen(rohurl)
        for l in results.readlines():
            try:
                if l.count('Matinee')>0:
                    timeslist[0] = timeslist[0]+1
                elif l.count('Evening')>0:
                    timeslist[1] = timeslist[1]+1
            except UnicodeDecodeError:
                print "Ignoring UnicodeDecodeError"
        print("Page " + str(i+1) + " parsed!")
        results.close()
    return timeslist

times = get_piece_times()
print("Matinee: " + str(times[0]))
print("Evening: " + str(times[1]))
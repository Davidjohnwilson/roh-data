import urllib2


def gather_data(num_pages=367):
    results = []

    for i in range(0, num_pages + 1):
        rohurl = "http://www.rohcollections.org.uk/"
        rohurl += "SearchResults.aspx?searchtype=performance"
        rohurl += "&company=The%20Royal%20Ballet&genre=Ballet&page="
        rohurl += str(i)
        page = urllib2.urlopen(rohurl)
        date_str = ''
        matinee_evening_str = ''
        piece_str = ''
        for l in page.readlines():
            try:
                if l.count('<td>') > 0 and l.count("<a href='performance.") > 0 and l.count('<td>The Royal Ballet</td>') == 0 and l.count('<td>Matinee</td>') == 0 and l.count('<td>Evening</td>') == 0:
                    date = l.split("page=" + str(i) + "'>")[-1]
                    date = date.split('</a>')[0]
                    date = date.split('<a')[1]
                    date = date.split('>')[1]
                    date_str = date
                if l.count('<td>') > 0 and l.count('<a href') == 0 and l.count('<td>The Royal Ballet</td>') == 0 and l.count('<td>Matinee</td>') == 0 and l.count('<td>Evening</td>') == 0:
                    corename = l.split('<td>')[-1].split('</td>')[0]
                    piece_str = corename
                if l.count('Matinee') > 0:
                    matinee_evening_str = 'Matinee'
                elif l.count('Evening') > 0:
                    matinee_evening_str = 'Evening'
            except UnicodeDecodeError:
                print("Ignoring UnicodeDecodeError")
            if matinee_evening_str != '':
                summary_str = ','.join([date_str,
                                        matinee_evening_str,
                                        piece_str])
                print(summary_str)
                results.append(summary_str)
                date_str = ''
                matinee_evening_str = ''
                piece_str = ''

        print("Page " + str(i + 1) + " parsed!")
        page.close()

    return results


def save_data(filename='./data.csv', num_pages=367):
    results = ['Date,Time,Piece']
    results += gather_data(num_pages)

    myfile = open(filename, 'w')
    for r in results:
        myfile.write(r + '\n')
    myfile.close

gather_data(1)
# save_data('./data/data.csv', 10)

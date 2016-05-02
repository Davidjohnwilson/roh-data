from bs4 import BeautifulSoup
import urllib
import csv


#We first try to find the list of performances

data_object_list = []

for i in xrange(0, 368):
    try:
        rohurl = "http://www.rohcollections.org.uk/"
        rohurl += "SearchResults.aspx?searchtype=performance"
        rohurl += "&company=The%20Royal%20Ballet&genre=Ballet&page="
        rohurl += str(i)

        r = urllib.urlopen(rohurl).read()
        soup = BeautifulSoup(r)

        performances = soup.find_all("tr", class_=["odd","even"])
        for p in performances:
            data = p.get_text().split('\n')[1:-1]
            encoded_data = [d.encode("utf-8") for d in data]
            data_object = {}
            data_object['piece'] = encoded_data[0]
            data_object['date'] = encoded_data[1]
            data_object['mateve'] = encoded_data[2]
            data_object['company'] = encoded_data[3]
            data_object_list.append(data_object)

        with open("./data/performance_data.csv", "w") as toWrite:
            writer = csv.writer(toWrite, delimiter=",")
            csv_keys = ["date", "mateve", "piece", "company"]
            writer.writerow(csv_keys)
            for d_o in data_object_list:
                writer.writerow([d_o[k] for k in csv_keys])

    except IOError:
        print("No internet connection")

data_object_list = []

for i in xrange(0,20):
    try:
        rohurl = "http://www.rohcollections.org.uk/"
        rohurl += "SearchResults.aspx?searchtype=work"
        rohurl += "&company=The%20Royal%20Ballet&genre=Ballet&page="
        rohurl += str(i)

        r = urllib.urlopen(rohurl).read()
        soup = BeautifulSoup(r)

        pieces = soup.find_all("tr", class_=["odd","even"])
        for p in pieces:
            data = p.get_text().split('\n')[1:-1]
            encoded_data = [d.encode("utf-8") for d in data]
            components = encoded_data[-1].split(' (')
            choreographer = components[-1].split(')')[0]
            piece = ' ('.join(components[:-1])
            data_object = {}
            data_object['genre'] = encoded_data[0]
            data_object['piece'] = piece
            data_object['choreographer'] = choreographer
            data_object_list.append(data_object)

        with open("./data/choreographer_data.csv", "w") as toWrite:
            writer = csv.writer(toWrite, delimiter=",")
            csv_keys = ["genre", "piece", "choreographer"]
            writer.writerow(csv_keys)
            for d_o in data_object_list:
                writer.writerow([d_o[k] for k in csv_keys])
    except IOError:
        print("No internet connection")


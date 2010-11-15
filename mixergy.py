import os,sys,csv,urllib,time,re
from BeautifulSoup import BeautifulSoup

base_url = 'http://mixergy.com/interviews/page/2/'

def getUrls(url):
    print "Getting ",url
    data = urllib.urlopen( url )
    text = data.read()
    text = text.replace("\r","")
    text = text.replace("\n","")
    
    print text
    soup = BeautifulSoup( text )
    d = soup.findAll('h2', {'class':'title '})
    print d
    new_url = ''
    for dd in d:
        x = dd.find('a')
        print x['href']
        new_url = x['href']
    findMP3(new_url)
        
def findMP3(url):
    print "Getting ",url
    data = urllib.urlopen( url )
    text = data.read()
    text = text.replace("\r","")
    text = text.replace("\n","")
    soup = BeautifulSoup( text )
    
    link = soup.find('a', {'href': re.compile('mp3')})
    print link['href']
    
def main(argv=None):
    #if argv is None:
    #    argv = sys.argv
    #process_file( argv[1], argv[2] )
    #process_file('/dev/geo_data/geo_data.csv', '/dev/geo_data/geo_data_out.csv' )
    getUrls(base_url)

if __name__ == '__main__':
    #main(sys.argv)
    main()

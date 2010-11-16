import os,sys,csv,urllib,time,re,itertools
from BeautifulSoup import BeautifulSoup

class MixergyMP3Retriever:
    def __init__(self):
        pass

    def getListingUrls(self,start_pg, end_pg):
        return ['http://mixergy.com/interviews/page/%d/' % i for i in range(start_pg,end_pg+1)]

    def getIndividualUrls(self,listing_url):
        print "Getting",listing_url
        data = urllib.urlopen( listing_url )
        time.sleep(3)
        text = data.read().replace("\r","").replace("\n","")
        soup = BeautifulSoup( text )
        return [d.find('a')['href'] for d in soup.findAll('h2', {'class':'title '})]
        
    def findMP3Url(self,url):
        print "Getting",url
        data = urllib.urlopen( url )
        time.sleep(3)
        text = data.read().replace("\r","").replace("\n","")
        soup = BeautifulSoup( text )
        #link = soup.find('a', {'href': re.compile('mp3')})
        return soup.find('a', {'href': re.compile('mp3')})['href']
        #print link['href']
    
def main(argv=None):
#    m = MixergyMP3Retriever()
#    listing_urls = m.getListingUrls(1, 1)
    #individual_urls = [m.getIndividualUrls(listing_url) for listing_url in listing_urls]
#    individual_urls = list(itertools.chain(*[m.getIndividualUrls(listing_url) for listing_url in listing_urls]))
#    print len(individual_urls),"-",individual_urls
#    mp3_urls = [m.findMP3Url(url) for url in individual_urls]
#    print len(mp3_urls),"-",mp3_urls
    urllib.urlretrieve('http://mixergy.com/wp-content/audio/Rob-Rawson-(TimeDoctor)-on-Mixergy.mp3', '/dev/mixergy/temp.mp3')
    
    #if argv is None:
    #    argv = sys.argv
    #process_file( argv[1], argv[2] )
    #process_file('/dev/geo_data/geo_data.csv', '/dev/geo_data/geo_data_out.csv' )
    #getUrls(base_url)

if __name__ == '__main__':
    #main(sys.argv)
    main()

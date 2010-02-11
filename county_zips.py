import os,sys,csv,urllib,time,re
from BeautifulSoup import BeautifulSoup

base_url = 'http://www.melissadata.com/lookups/CountyZip.asp?fips=%s&submit1=Submit'

def process_file(infile, outfile):
    f = file(infile, 'r')
    reader = csv.reader(f)

    row = 0
    all_fips = []
    for line in reader:
        if row == 0:
            header = line
        else:
            (name,state_name,state_fips,cnty_fips,fips,area,fips_num) = line
            all_fips.append(fips)
        row += 1
    f.close()

    print all_fips
    all_fips = all_fips[:2]

    f = file(outfile,'w')
    f.write("fips\tzip\tcity\tpercent\n")
    for fips in all_fips:
        results = get_fips_info( fips )
        for result in results:
            f.write(fips + "\t" + "\t".join(result)+"\n")
    f.close()

def get_fips_info(fips):
    url = base_url % fips
    print 'Processing',url

    path = '/tmp/%s.txt' % fips
    
    if os.path.exists( path ):
        f = file(path,'r')
        text = f.read()
        f.close()
    else:
        data = urllib.urlopen( url )
        text = data.read()
        text = text.replace("\r","")
        text = text.replace("\n","")
        text = re.sub(R'.+?<html>', '<html>', text)
        text = re.sub(R'<script.+?</script>', '', text)
        f = file(path,'w')
        f.write( text )
        f.close()
        time.sleep(10)
    
    soup = BeautifulSoup( text )
    
    results = []
    for info in soup.findAll('tr',{'bgcolor':'#e0eaf3'}):
        (zip,city,percent) = info.findAll('td')[:3]
        print zip.a.string,city.string,percent.string
        results.append([zip.a.string,city.string,percent.string])
        
    for info in soup.findAll('tr',{'bgcolor':'#ffffff'}):
        (zip,city,percent) = info.findAll('td')[:3]
        print zip.a.string,city.string,percent.string
        results.append([zip.a.string,city.string,percent.string])
        
    return results

def main(argv=None):
    if argv is None:
        argv = sys.argv
    process_file( argv[1], argv[2] )

if __name__ == '__main__':
    main(sys.argv)

# python county_zips.py geo_data.csv geo_data_out.csv

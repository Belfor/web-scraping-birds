import getopt, sys
from scraper import Scraper

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:],'r:f:l:',
        ['region=',
        'filename=',
        'limit='])
        region = 'ES'
        filename = 'birds.csv'
        limit = 5
        for opt, arg in opts:
            if opt in ('-r', '--region'):
                region = arg
            elif opt in ('-f', '--filename'):
                filename = arg
            elif opt in ('-l', '--limit'):
                limit = int(arg)
            else:
                sys.exit(2)
        print(region)
        print(filename)
        print(limit)
        scr = Scraper(region=region, filename=filename,limit=limit)
        scr.extract()
    except:
        sys.exit(2)

 

    
import logging
import sys
import random
import os

def main():
    # set up logging to file and directories
    try: 
        os.mkdir("logs")
    except OSError as error: 
        logging.debug("logs directory already exists")
    try: 
        os.mkdir("testData")
    except OSError as error: 
        logging.debug("logs directory already exists")
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        filename='logs/testData.log',
                        filemode='w')
    
    # create test data
    logging.debug("creating test data")
    args = sys.argv[1:]
    size = args.pop(0)

    logging.debug("opening file")
    file = open("testData/testData.txt", "w")
    for i in range(int(size)):
        file.write(str(args[random.randint(0, len(args)-1)]) + "\n")

    logging.debug("closing file")
    file.close()
    return 0
    
if __name__ == '__main__':
    main()
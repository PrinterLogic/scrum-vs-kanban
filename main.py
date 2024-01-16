import os
import logging
from kanban import Kanban
from scrum import Scrum

def main():
    # set up logging to file
    try: 
        os.mkdir("logs")
    except OSError as error: 
        logging.debug("logs directory already exists")
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        filename='logs/main.log',
                        filemode='w')
    logging.debug("python main function")

    test_agile = os.environ.get("SVK_TEST_AGILE")
    if test_agile == None:
        test_agile = "kanban"
        os.environ["SVK_TEST_AGILE"] = test_agile

    # gather test data
    test_data = open("testData/testData.txt", "r")
    test_data_list = test_data.read().splitlines()
    test_data.close()
    logging.debug("test data: " + str(test_data_list))

    # testing kanban:
    if test_agile == "kanban":
        kanban = Kanban()
        kanban.run(test_data_list)
    # testing scrum:
    elif test_agile == "scrum":
        scrum = Scrum()
        scrum.run(test_data_list)

    return 0

if __name__ == '__main__':
    main()
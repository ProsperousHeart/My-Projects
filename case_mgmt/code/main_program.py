__copyright__ = "Copyright (c) 2022 Prosperous Heart, LLC. All rights reserved."
__author__ = "Kassandra Keeton"
__version__ = "1.0.0"
__maintainer__ = "Kassandra Keeton"
__status__ = "WIP"

# from classes import Flag, Case_Obj, Engineer
from temp_data import engr_ids as engrs
from temp_data import case_db as db_client
from temp_data import case_status
# from temp_data import case_status as status_list
from utilities import get_case_data, get_engr_data

import webbrowser

# debugging packages
import snoop
# from loguru import logger as loguru_logger

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

status_dict = {str(num): item for num, item in enumerate(case_status)}


def req_Info():
    """
    This function requests data and returns a tuple of 2 strings.
    First element is the ID looking for.
    2nd element is if the ID needs to be exact.

    """
    while True:
        engr_id = input("What engineer ID are you looking for?\t")
        if engr_id == "":
            print("Please provide a valid engineer ID.")
        else:
            break

    while True:
        exact_match = input("Does this need to be exact? 1 - Yes, 2 - No\t")
        if exact_match not in ["1", "2"]:
            print("Please provide a 1 or 2")
        else:
            if exact_match == "1":
                return engr_id, True
            return engr_id, False


def locate_Engr(chk_id: str = None, exact: bool = False):
    """
    This function checks to see if an engineer's ID is in the system.
    If it is, returns ID. Otherwise returns None.
    """

    if exact:
        return [item for item in engrs if chk_id == item['id']]
    return [item for item in engrs if chk_id in item['id']]


# @snoop
def det_status():
    """
    This function inquires the status of cases they are looking for.
    Returns the requested status.
    """

    while True:
        ask_status = input(f"Which status would you like to pull cases for?\n{status_dict}\t")
        if ask_status not in status_dict.keys():
            print("Please choose a number related to a case status.")
        else:
            return status_dict[ask_status]


# @loguru_logger.catch
@snoop
def process_data(engr_dict: dict, status_val):
    """

    """

    # ==============================================================
    # pull case data for engineer as per user request
    # ==============================================================
    # logger.debug('Attempting to call get_engr_data()...')
    engr_case_data = get_case_data(db_client, engr_dict['id'], status_val)
    if len(engr_case_data) == 0:
        print(f"There are no cases for engineer ID {engr_dict['id']} with '{status_val}' status.")
    else:
        # print(engr_case_data)

        # this section will be to show the HTML created file in browser
        # https://stackoverflow.com/a/19002247/10474024
        # https://stackoverflow.com/a/40905794/10474024
        # webbrowser.open("https:/prosperousheart.com", new=2, autoraise=True)
        print("Not yet opening web browser with Jira2 output.")


# This section wil allow python file to be run from command line
if __name__ == "__main__":
    """
    This function is only executed if run as a script.
    
    """

    # ==============================================================
    # request from user:
    #     - the ID of the engineer they are looking for
    #     - if they are looking for an exact match or partial number
    # ==============================================================
    engr_id, exact_bool = req_Info()

    # ==============================================================
    # confirm if engineer exists
    # ==============================================================
    engr_list = locate_Engr(engr_id, exact_bool)
    del exact_bool
    del engr_id

    if len(engr_list) == 0:
        print("No engineers found.")
    elif len(engr_list) == 1:
        process_data(engr_list[0], det_status())
    else:
        # this should never happen - database should have unique engineer numbers
        print("ERROR! Multiple engineers")

    print("Data has been processed. Program ending.\n")

__copyright__ = "Copyright (c) 2022 Prosperous Heart, LLC. All rights reserved."
__author__ = "Kassandra Keeton"
__version__ = "1.0.0"
__maintainer__ = "Kassandra Keeton"
__status__ = "WIP"

# from classes import Flag, Case_Obj, Engineer
from temp_data import engr_ids as engrs

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def locate_Engr(chk_id: str = None, exact:bool = False):
    """
    This function checks to see if an engineer's ID is in the system.
    If it is, returns ID. Otherwise returns None.
    """

    if exact:
        return [item for item in engrs if chk_id == item['id']]
    return [item for item in engrs if chk_id in item['id']]

def req_Info():
    """
    This function requests data and returns a tuple of 2 strings.
    First element is the ID looking for.
    2nd element is if the ID needs to be exact.

    """
    engr_id = input("What engineer ID are you looking for?\t")

    while True:
        exact_match = input("Does this need to be exact? 1 - Yes, 2 - No\t")
        if exact_match not in ["1", "2"]:
            print("Please provide a 1 or 2")
        else:
            if exact_match == "1":
                return (engr_id, True)
            return (engr_id, False)

# This section wil allow python file to be run from command line
if __name__ == "__main__":
    """
    This function is only executed if run as a script.
    
    """

    engr_id, exact_bool = req_Info()
    engr_list = locate_Engr(engr_id, exact_bool)
    del exact_bool

    if len(engr_list) == 0:
        print("No engineers found.")
    elif len(engr_list) == 1:
        print(engr_list[0])
    else:
        print("ERROR! Multiple engineers")
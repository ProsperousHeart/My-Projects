__copyright__ = "Copyright (c) 2022 Prosperous Heart, LLC. All rights reserved."
__author__ = "Kassandra Keeton"
__version__ = "1.0.0"
__maintainer__ = "Kassandra Keeton"
__status__ = "WIP"

from collections import OrderedDict

# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)


def get_case_data(db_client, engineer_id:str, status:str = "Open"):
    """
    This function will send a call to a database and return all cases
    currently not closed and assigned to requested engineer.

    """

    # right now, db_client is a list of dictionaries
    if status == "All":
        return [(item, status) for item in db_client if item['engr_id'] == engineer_id]
    else:
        return [(item, status) for item in db_client if item['engr_id'] == engineer_id and item['status'] == status]

def get_engr_data(engr_id, db_client):
    """
    This function gathers all of the open cases for the engineer.

    Returns Engineer() class item - no flags completed, just empty setup.

    """

    # logger.debug('Starting get_engr_data()...')

    engr_data = None
    new_cases = None
    update_cases = None
    curr_case_docs_db = None

    # db_client = case_db    # temporary until real database created

    # pull cases by engineer - specific pieces of required data
    case_list = get_case_data(db_client, engr_id)

    # logger.debug('Ending get_engr_data() and returning:  %s', (engr_data, curr_case_docs_db))
    return case_list
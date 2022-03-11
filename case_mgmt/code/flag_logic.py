__copyright__ = "Copyright (c) 2022 Prosperous Heart, LLC. All rights reserved."
__author__ = "Kassandra Keeton"
__version__ = "1.0.0"
__maintainer__ = "Kassandra Keeton"
__status__ = "WIP"

# if you're not using pytest, though logging could still be crucial
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

flag_type_list = ['cu_req_esc_flag',
                  'cu_req_update_flag',
                  'dm_flag',
                  'esc_to_bu_flag',
                  'hold_status',
                  'last_ext_update_flag',
                  'last_reviewed',
                  'total_age_flag']
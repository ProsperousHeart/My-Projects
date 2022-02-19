engr_ids = [{'id':"1234", 'f_name':"Rory", 'l_name':'Gilmore'},
            {'id':"5678", 'f_name':"Daniel", 'l_name':'Fizzlestick'}
            ]

# temporary "database"
case_db = [
    {'case_no': 123, 'createdDate': "2022-02-01", 'pri': "3",
     'status': "Open", 'lastModDate': "2022-02-18", 'engr_id': "1234"},
    {'case_no': 124, 'createdDate': "2022-02-01", 'pri': "2",
     'status': "Closed", 'lastModDate': "2022-02-18", 'engr_id': "1234"},
    {'case_no': 125, 'createdDate': "2022-02-18", 'pri': "2",
     'status': "Open", 'lastModDate': "2022-02-18", 'engr_id': "1234"}
]

case_status = ["Open", "Closed", "Escalated - BU", "Escalated - DM",
               "On Hold", "Closed", "Reopened"]
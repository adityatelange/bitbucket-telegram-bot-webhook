
def pullrequest(event_sub_type, data_json):
    return globals()[event_sub_type](data_json)

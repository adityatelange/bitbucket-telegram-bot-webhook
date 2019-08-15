from EventHandler.issue.comment_created import comment_created
from EventHandler.issue.created import created
from EventHandler.issue.updated import updated


def issue(event_sub_type, data_json):
    return globals()[event_sub_type](data_json)

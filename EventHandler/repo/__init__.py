from EventHandler.repo.commit_comment_created import commit_comment_created
from EventHandler.repo.commit_status_created import commit_status_created
from EventHandler.repo.commit_status_updated import commit_status_updated
from EventHandler.repo.fork import fork
from EventHandler.repo.push import push
from EventHandler.repo.transfer import transfer
from EventHandler.repo.updated import updated


def repo(event_sub_type, data_json):
    # web-hooks for the following events that occur in a repository.
    return globals()[event_sub_type](data_json)

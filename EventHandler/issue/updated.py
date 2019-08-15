def updated(data_json):
    # A user updated an issue for a repository
    repository = data_json['repository']
    # repository_scm = repository['scm']
    repository_name = repository['name']
    repository_link = repository['links']['html']['href']

    # actor = data_json['actor']
    # actor_name = actor['display_name']
    # actor_profile = actor['links']['html']['href']

    issue = data_json['issue']

    issue_title = issue['title']
    issue_priority = issue['priority']
    if 'assignee' in issue:
        if issue['assignee']:
            issue_assignee_name = issue['assignee']['display_name']
            issue_assignee_link = issue['assignee']['links']['html']['href']
        else:
            issue_assignee_name = "' '"
            issue_assignee_link = "' '"
    else:
        issue_assignee_name = "' '"
        issue_assignee_link = "' '"
    issue_reporter_name = issue['reporter']['display_name']
    issue_reporter_link = issue['reporter']['links']['html']['href']
    issue_description = issue['content']['raw']
    issue_created_on = issue['created_on']
    issue_link = issue['links']['html']['href']

    changes = data_json['changes']

    status_old = changes['status']['old']
    status_new = changes['status']['new']
    message = "Issue Edited in [{}]({}) " \
              " \nTitle: [{}]({}) " \
              "\nPriority: *{}* " \
              "\nReporter: [{}]({}) " \
              "\nAssignee: [{}]({}) " \
              "\nCreated On: {}" \
              "\nStatus Changed from _{}_ to _{}_ " \
              "\nDescription: {}".format(repository_name, repository_link, issue_title, issue_link, issue_priority,
                                         issue_reporter_name, issue_reporter_link, issue_assignee_name,
                                         issue_assignee_link, issue_created_on,
                                         status_old, status_new,
                                         issue_description)
    return message

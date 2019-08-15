def comment_created(data_json):
    # A user comments on an issue associated with a repository.
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
    issue_assignee_name = issue['assignee']['display_name']
    issue_assignee_link = issue['assignee']['links']['html']['href']
    issue_reporter_name = issue['reporter']['display_name']
    issue_reporter_link = issue['reporter']['links']['html']['href']
    issue_description = issue['content']['raw']
    issue_created_on = issue['created_on']
    issue_link = issue['links']['html']['href']

    comment = data_json['comment']

    # user details
    user_name = comment['user']['display_name']
    user_profile = comment['user']['links']['html']['href']

    # actual comment
    comment_content = comment['content']['raw']

    # parent comment
    parent_comment_msg = " "
    try:
        parent_comment = comment['parent']['id']
        parent_comment_link = comment['parent']['links']['html']['href']
        parent_comment_msg = "\nparent comment: [{}]({})".format(parent_comment, parent_comment_link)
    except KeyError:
        pass

    message = "[{}]({}) commented on an Issue Created in [{}]({}) " \
              " \nTitle: [{}]({}) " \
              "\nComment : *{}* " \
              "{} " \
              "\nPriority: *{}* " \
              "\nReporter: [{}]({}) " \
              "\nAssignee: [{}]({}) " \
              "\nCreated On: {}" \
              "\nDescription: {}".format(user_name,
                                         user_profile,
                                         repository_name,
                                         repository_link,
                                         issue_title,
                                         issue_link,
                                         comment_content,
                                         parent_comment_msg,
                                         issue_priority,
                                         issue_reporter_name,
                                         issue_reporter_link,
                                         issue_assignee_name,
                                         issue_assignee_link,
                                         issue_created_on,
                                         issue_description)
    return message

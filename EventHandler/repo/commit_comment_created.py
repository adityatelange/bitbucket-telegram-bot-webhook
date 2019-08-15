def commit_comment_created(data_json):
    # Commit comment created
    # A user comments on a commit in a repository.
    repository = data_json['repository']
    # repository_scm = repository['scm']
    repository_name = repository['name']
    repository_link = repository['links']['html']['href']

    # actor = data_json['actor']
    # actor_name = actor['display_name']
    # actor_profile = actor['links']['html']['href']

    comment = data_json['comment']

    # user details
    user_name = comment['user']['display_name']
    user_profile = comment['user']['links']['html']['href']

    # actual comment
    comment_content = comment['content']['raw']

    # commit details
    commit = comment['commit']
    commit_hash = commit['hash']
    if len(commit_hash) > 7:
        commit_hash = commit_hash[:7]

    commit_link = commit['links']['html']['href']

    # parent comment
    parent_comment_msg = " "
    try:
        parent_comment = comment['parent']['id']
        parent_comment_link = comment['parent']['links']['html']['href']
        parent_comment_msg = "\nparent comment: [{}]({})".format(parent_comment, parent_comment_link)
    except KeyError:
        pass

    message = "[{}]({}) commented on a Commit \nComment : *{}* \nCommit: [{}]({}) {} \nRepository: [{}]({})". \
        format(user_name,
               user_profile,
               comment_content,
               commit_hash,
               commit_link,
               parent_comment_msg,
               repository_name,
               repository_link)

    return message

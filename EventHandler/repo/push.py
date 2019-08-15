def push(data_json):
    # A user pushes 1 or more commits to a repository.
    repository = data_json['repository']
    # repository_scm = repository['scm']
    repository_name = repository['name']
    repository_link = repository['links']['html']['href']

    actor = data_json['actor']
    actor_name = actor['display_name']
    actor_profile = actor['links']['html']['href']

    pushh = data_json['push']['changes'][0]

    push_forced = pushh['forced']
    push_created = pushh['created']
    push_truncated = pushh['truncated']
    push_closed = pushh['closed']

    push_commits_all = pushh['commits']

    commits_str = ""
    for commit in push_commits_all:
        commit_hash = commit['hash']
        if len(commit_hash) > 7:
            commit_hash = commit_hash[:7]
        commit_link = commit['links']['html']['href']
        # commit_summary = commit['summary']['raw']
        commit_message = commit['message']
        # commit_author_name = commit['author']['user']['display_name']
        # commit_author_link = commit['author']['user']['links']['html']['href']

        commits_str += '\n\t#{} [{}]({}) \n=> _{}_'.format(push_commits_all.index(commit),
                                                           commit_hash, commit_link,
                                                           commit_message)
    push_link = pushh['links']['html']['href']

    push_new = pushh['new']
    push_old = pushh['old']

    message = "[{}]({}) pushed to [{}]({})" \
              " \nCompare: [compare]({})" \
              " \nCommits: \n{}".format(actor_name,
                                        actor_profile,
                                        repository_name,
                                        repository_link,
                                        push_link,
                                        commits_str
                                        )

    return message

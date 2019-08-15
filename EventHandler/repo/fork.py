def fork(data_json):
    # A user forks a repository.

    # repository = data_json['repository']
    # repository_scm = repository['scm']
    # repository_name = repository['name']
    # repository_link = repository['links']['html']['href']

    actor = data_json['actor']
    actor_name = actor['display_name']
    actor_profile = actor['links']['html']['href']

    forkk = data_json['fork']

    fork_parent_full_name = forkk['parent']['full_name']
    fork_parent_link = forkk['parent']['links']['html']['href']
    fork_full_name = forkk['full_name']
    fork_link = forkk['links']['html']['href']

    message = "[{}]({}) forked to [{}]({}) by [{}]({})".format(fork_parent_full_name,
                                                               fork_parent_link,
                                                               fork_full_name,
                                                               fork_link,
                                                               actor_name,
                                                               actor_profile
                                                               )
    return message

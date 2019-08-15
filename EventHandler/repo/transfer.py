def transfer(data_json):
    # A repository transfer is accepted.

    repository = data_json['repository']
    # repository_scm = repository['scm']
    repository_name = repository['name']
    repository_link = repository['links']['html']['href']

    # is the current owner who accepted transfer
    actor = data_json['actor']
    actor_name = actor['display_name']
    actor_profile = actor['links']['html']['href']

    previous_owner = data_json['previous_owner']
    previous_owner_name = previous_owner['display_name']
    previous_owner_profile = previous_owner['links']['html']['href']

    message = "[{}]({}) transferred to [{}]({}) from [{}]({})".format(
        repository_name, repository_link, actor_name, actor_profile, previous_owner_name, previous_owner_profile
    )

    return message

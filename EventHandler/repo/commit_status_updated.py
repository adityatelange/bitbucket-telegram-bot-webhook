def commit_status_updated(data_json):
    # Build status updated
    # A build system, CI tool, or another vendor recognizes that a commit has a new status and ...
    # ... updates the commit with its status.

    repository = data_json['repository']
    # repository_scm = repository['scm']
    repository_name = repository['name']
    repository_link = repository['links']['html']['href']

    actor = data_json['actor']
    actor_name = actor['display_name']
    actor_profile = actor['links']['html']['href']

    commit_status = data_json['commit_status']

    name = commit_status['name']
    description = commit_status['description']
    state = commit_status['state']
    url = commit_status['url']
    typee = commit_status['type']

    message = "Build status updated on [{}]({}) by [{}]({})" \
              " \nName: {} " \
              " \nState: {}" \
              " \nType: {}" \
              " \nDescription: {}" \
              " \nUrl to the vendor: {}".format(repository_name,
                                                repository_link,
                                                actor_name,
                                                actor_profile,
                                                name,
                                                state,
                                                typee,
                                                description,
                                                url
                                                )

    return message

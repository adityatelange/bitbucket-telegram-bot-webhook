def updated(data_json):
    # A user updates the  Name ,  Description ,  Website , or  Language  fields under ...
    # ... the  Repository details  page of the repository settings.

    repository = data_json['repository']
    # repository_scm = repository['scm']
    repository_name = repository['name']
    repository_link = repository['links']['html']['href']

    actor = data_json['actor']
    actor_name = actor['display_name']
    actor_profile = actor['links']['html']['href']

    changes = data_json['changes']
    changes_str = ""
    if 'name' in changes:
        change_name = changes['name']
        changes_str += " \nName: from *{}* to *{}* ".format(
            "' '" if change_name['old'] == "" else change_name['old'], change_name['new'])

    if 'website' in changes:
        change_website = changes['website']
        changes_str += " \nWebsite: from *{}* to *{}* ".format(
            "' '" if change_website['old'] == "" else change_website['old'],
            change_website['new'])

    if 'language' in changes:
        change_language = changes['language']
        changes_str += " \nLanguage: from *{}* to *{}* ".format(
            "' '" if change_language['old'] == "" else change_language['old'],
            change_language['new'])

    if 'links' in changes:
        changes_links = changes['links']
        if changes_links['old'] and changes_links['old']:
            changes_str += " \nLinks: from *{}* to *{}* ".format(
                "' '" if changes_links['old']['html']['href'] == "" else changes_links['old']['html']['href'],
                changes_links['new']['html']['href'])

    if 'description' in changes:
        change_description = changes['description']
        changes_str += " \nDescription: from *{}* to *{}* ".format(
            "' '" if change_description['old'] == "" else change_description['old'],
            change_description['new'])

    if 'full_name' in changes:
        change_full_name = changes['full_name']
        changes_str += " \nFull Name: from *{}* to *{}* ".format(
            "' '" if change_full_name['old'] == "" else change_full_name['old'],
            change_full_name['new'])

    if 'has_issues' in changes:
        change_has_issues = changes['has_issues']
        changes_str += " \nHas Issues: from *{}* to *{}* ".format(
            "' '" if change_has_issues['old'] == "" else change_has_issues['old'], change_has_issues['new'])

    if 'fork_policy' in changes:
        change_fork_policy = changes['fork_policy']
        changes_str += " \nFork Policy: from *{}* to *{}* ".format(
            "' '" if change_fork_policy['old'] == "" else change_fork_policy['old'], change_fork_policy['new'])

    message = "[{}]({}) updated repository settings of [{}]({}) " \
              "{}".format(actor_name,
                          actor_profile,
                          repository_name,
                          repository_link,
                          changes_str
                          )

    return message

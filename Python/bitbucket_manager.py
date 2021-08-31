from argparse import ArgumentParser
import requests
import re
import time


def normalize_name(project_name):
    """
    Remove any and all special characters and concatenates space-divided word with underscores

    Params:
    project_name | string | Word or Phrase that will be normalized

    Returns:
    string | A normalized word/phrase with no special characters and underscores instead of spaces
    """
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+', project_name)

    return '_'.join(map(str.upper, words))


def bitbucket_manager(bitbucket_username, bitbucket_password, bitbucket_team, bitbucket_project_name, bitbucket_repository_name):
    bitbucket_auth = (bitbucket_username, bitbucket_password)
    project_key = normalize_name(bitbucket_project_name)
    repository_name = bitbucket_repository_name

    headers = {'Accept-Charset': 'ISO-8859-1', 'X-Atlassian-Token': 'nocheck'}
    project_options = {"name": bitbucket_project_name, "key": project_key, "is_private": True}

    project_response = requests.post(url="https://api.bitbucket.org/2.0/workspaces/{}/projects/".format(bitbucket_team),
                                     json=project_options, auth=bitbucket_auth, headers=headers)

    if project_response.status_code == 200 or project_response.status_code == 201:
        print('Project "{}" was created successfully'.format(bitbucket_project_name))
    else:
        if project_response.status_code == 401:
            print('Error creating project "{}". Authentication failed'.format(bitbucket_project_name))
        else:
            print(project_response.status_code)
            print(project_response.response)
            project_response_json = project_response.json()
            print('Error creating project "{}"'.format(bitbucket_project_name))
            print(project_response_json)
            exit(1)

    time.sleep(5)
    repository_options = {"has_wiki": True, "scm": "git", "is_private": True, "project": {"key": project_key}}
    bitbucket_project_endpoint = "https://api.bitbucket.org/2.0/repositories/{}/{}" \
        .format(bitbucket_team, repository_name)
    repository_response = requests.post(url=bitbucket_project_endpoint, json=repository_options, auth=bitbucket_auth)

    if repository_response.status_code == 200 or repository_response.status_code == 201:
        print('Repository "{}" was created successfully'.format(repository_name))
    else:
        if project_response.status_code == 401:
            print('Error creating repository "{}". Authentication Failed'.format(repository_name))
        else:
            repository_response_json = repository_response.text
            print('Error creating repository "{}"'.format(repository_name))
            print(repository_response_json)
            exit(1)

    exit(0)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-u", "--username", dest="bitbucket_username", required=True,
                        help="Bitbucket username")
    parser.add_argument("-p", "--password", dest="bitbucket_password", required=True,
                        help="Bitbucket password")
    parser.add_argument("--team", dest="bitbucket_team", required=True,
                        help="Bitbucket Team/User")
    parser.add_argument("--project", dest="bitbucket_project_name", required=True,
                        help="Bitbucket Project Name")
    parser.add_argument("--repository", dest="bitbucket_repository_name", required=True,
                        help="Bitbucket Repository Name")

    args = parser.parse_args()

    bitbucket_manager(args.bitbucket_username, args.bitbucket_password,
                      args.bitbucket_team, args.bitbucket_project_name,
                      args.bitbucket_repository_name)

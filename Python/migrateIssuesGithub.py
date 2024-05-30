__version__ = "1.0.0"

import requests as rq
from copy import deepcopy
from time import sleep
from requests import HTTPError
import re

GITHUB_API_TOKEN = ""
GITHUB_BASE_URL = "https://api.github.com"
# Github Request Headers
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-Github-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {GITHUB_API_TOKEN}"
}


def pullIssues(owner, originRepo):
    # Define our request parameters
    params = {
        "per_page": 300,
        "state": "all"
    }

    # Build the entire URL to pull issues from the origin repository
    listRepoIssuesURL = f"{GITHUB_BASE_URL}/repos/{owner}/{originRepo}/issues"

    # Get the list of issues in the origin repository assigned to the Owner passed
    try:
        response = rq.get(listRepoIssuesURL, headers=HEADERS, params=params)
        response.raise_for_status()
    except HTTPError as err:
        print("Request error: " + err)

    # Get returned issues and the response headers
    issueList = response.json()
    responseHeaders = response.headers

    # Check if pagination is needed/enabled/used
    paginationEnabled = False
    if "link" in responseHeaders:
        paginationEnabled = True

    # Pull all issue pages
    while True:
        # If pagination is not enabled, we already pulled all issues, just return
        if not paginationEnabled:
            break

        # Build a pagination controller
        paginationController = {}
        linkList = responseHeaders["link"].split(",")
        for link in linkList:
            components = link.split(";")

            link = components[0].strip(" ").lstrip("<").rstrip(">")
            rel = re.search(r"(?<=rel=\")[a-z]*", components[1].strip(" ")).group(0)

            paginationController[rel] = link

        # If we reached the last page, end the loop
        if "next" not in paginationController.keys():
            break

        # Get the next page link and call it
        try:
            nextPageResponse = rq.get(paginationController["next"], headers=HEADERS)
            nextPageResponse.raise_for_status()
        except HTTPError as err:
            print("Request error: " + err)

        responseHeaders = nextPageResponse.headers
        nextPageIssues = nextPageResponse.json()

        # Append current page's issues to our issue list
        issueList += nextPageIssues

    return issueList


def cleanIssueList(issueList):
    # Map the necessary fields. Subfields are written in dot notation
    neededFields = [
        "title",
        "labels.name",
        "assignees.login",
        "milestone",
        "body",
        "comments_url",
        "number"
    ]

    # This is where our cleaned issues will be
    cleanedIssues = []

    # For each issue in our list, copy only important fields
    for issue in issueList:
        node = {}
        for field in neededFields:
            if "." in field:
                fieldParts = field.split(".")
                node[fieldParts[0]] = []

                for elem in issue[fieldParts[0]]:
                    node[fieldParts[0]].append(elem[fieldParts[-1]])
            else:
                node[field] = issue[field]

        cleanedIssues.append(node)

    return cleanedIssues


def createIssues(owner, destRepo, issueList):
    createIssueIDs = range(10, 310 + 1)

    # Build the entire URL to pull issues from the origin repository
    createIssueURL = f"{GITHUB_BASE_URL}/repos/{owner}/{destRepo}/issues"

    for issue in issueList:
        # Save the value of the issueID
        issueID = deepcopy(issue["number"])

        # Skip issues that we already created
        if issueID in createIssueIDs:
            continue

        # Move the comments_url field to a part of the body so we can keep track of what was migrated and remove unused fields
        issue["body"] += f"\r\n----------------------------{issue['comments_url']}"
        issue.pop("comments_url", None)
        issue.pop("number", None)

        # Create the issue in the destination repository
        try:
            print(f"Creating issue {issueID} in {destRepo}.")
            response = rq.post(createIssueURL, headers=HEADERS, json=issue)
            response.raise_for_status()
        except HTTPError as err:
            print(f"Request error - Issue {issueID} - Error: {err}")
            raise SystemExit(response.json(), response.headers)

        # Wait necessary interval to prevent rate-limiting
        sleep(4)


if __name__ == "__main__":
    print(f"Issue migration script - {__version__}")

    # Set our variables
    owner = ""
    originRepo = ""
    destRepo = ""

    # Pull all issues from the origin repository
    print(f"Pulling issues from {originRepo} that belongs to {owner}")
    originRepoIssueList = pullIssues(owner, originRepo)

    # Clean our issue list to remove unnecessary fields
    cleanedIssueList = cleanIssueList(originRepoIssueList)

    # Create these issues into our destination repository
    print(f"Creating {len(cleanedIssueList)} issues in {destRepo}")
    createIssues(owner, destRepo, cleanedIssueList)

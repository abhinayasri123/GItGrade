def generate_roadmap(repo_data, details):
    roadmap = []

    if not details["readme"]:
        roadmap.append("Add a detailed README with project overview and setup instructions.")

    if repo_data["commit_count"] < 10:
        roadmap.append("Commit code more frequently with meaningful commit messages.")

    if not repo_data["has_tests"]:
        roadmap.append("Add unit or integration tests to improve maintainability.")

    roadmap.append("Follow clean folder structure and modularize code.")
    roadmap.append("Improve documentation and code readability.")

    return roadmap

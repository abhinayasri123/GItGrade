def calculate_score(repo_data):
    score = 0
    details = {}

    if repo_data["has_readme"]:
        score += 20
        details["readme"] = True
    else:
        details["readme"] = False

    if repo_data["commit_count"] >= 10:
        score += 20

    if repo_data["file_count"] >= 5:
        score += 20

    if repo_data["has_tests"]:
        score += 15

    if len(repo_data["languages"]) >= 1:
        score += 15

    if repo_data["commit_count"] >= 20:
        score += 10

    return score, details

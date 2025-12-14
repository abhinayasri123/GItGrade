import requests
from scoring import calculate_score
from roadmap import generate_roadmap

def extract_repo_info(repo_url):
    parts = repo_url.replace("https://github.com/", "").split("/")
    owner, repo = parts[0], parts[1]

    base_url = f"https://api.github.com/repos/{owner}/{repo}"

    repo_info = requests.get(base_url).json()
    commits = requests.get(base_url + "/commits").json()
    languages = requests.get(base_url + "/languages").json()
    contents = requests.get(base_url + "/contents").json()

    has_readme = any("readme" in item["name"].lower() for item in contents)
    has_tests = any("test" in item["name"].lower() for item in contents)

    return {
        "commit_count": len(commits) if isinstance(commits, list) else 0,
        "languages": list(languages.keys()),
        "file_count": len(contents),
        "has_readme": has_readme,
        "has_tests": has_tests
    }

def get_level(score):
    if score >= 85:
        return "Advanced"
    elif score >= 60:
        return "Intermediate"
    else:
        return "Beginner"

def main():
    print("=== GitGrade Repository Analyzer ===")
    repo_url = input("Enter GitHub Repository URL: ")

    repo_data = extract_repo_info(repo_url)
    score, details = calculate_score(repo_data)
    level = get_level(score)
    roadmap = generate_roadmap(repo_data, details)

    print("\n--- ANALYSIS RESULT ---")
    print(f"Score: {score} / 100")
    print(f"Level: {level}")

    summary = "Project shows "
    summary += "good documentation. " if details["readme"] else "weak documentation. "
    summary += "Commit history is healthy." if repo_data["commit_count"] >= 10 else "Commit history needs improvement."

    print(f"\nSummary:\n{summary}")

    print("\nPersonalized Roadmap:")
    for step in roadmap:
        print(f"- {step}")

if __name__ == "__main__":
    main()

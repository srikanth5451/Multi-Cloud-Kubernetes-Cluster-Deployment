import os
import subprocess
from datetime import datetime, timedelta

def make_commit(commit_num, date):
    """Create a commit with proper email attribution"""
    # Create/modify a file
    with open("github_contributions.txt", "a") as f:
        f.write(f"Contribution {commit_num} at {date}\n")
    
    # Stage changes
    subprocess.run(["git", "add", "."])
    
    # Set commit metadata
    env = os.environ.copy()
    date_str = date.strftime("%a %b %d %H:%M:%S %Y +0000")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    env["GIT_AUTHOR_EMAIL"] = "basimsettysrikanth5451@gmail.com"
    env["GIT_COMMITTER_EMAIL"] = "basimsettysrikanth5451@gmail.com"
    env["GIT_AUTHOR_NAME"] = "srikanth5451"
    env["GIT_COMMITTER_NAME"] = "srikanth5451"
    
    # Create commit
    subprocess.run(["git", "commit", "-m", f"GitHub contribution {commit_num}"], env=env)

def main():
    # Initialize repository if needed
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])
        subprocess.run(["git", "branch", "-M", "main"])
    
    # Create 5 new test commits (visible in GitHub's 1-year graph)
    for i in range(1, 6):
        commit_date = datetime.now() - timedelta(days=i)
        make_commit(i, commit_date)
        print(f"Created commit {i}/5 for {commit_date.date()}")
    
    # Push to GitHub
    print("\nPushing to GitHub...")
    subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/srikanth5451/Multi-Cloud-Kubernetes-Cluster-Deployment.git"])
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"])

if __name__ == "__main__":
    main()
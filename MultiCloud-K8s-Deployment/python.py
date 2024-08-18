import os
import random
from datetime import datetime, timedelta
import subprocess

# Configuration - UPDATE THESE PATHS!
REPO_DIR = r"C:\Users\SRILUCKY\OneDrive\Desktop\my_github_projects\Multi-Cloud-Kubernetes-Cluster-Deployment\MultiCloud-K8s-Deployment"
USER_NAME = "Your Name"
USER_EMAIL = "your@email.com"

def verify_git_repo():
    """Check if we're in a git repo"""
    try:
        subprocess.run(["git", "rev-parse", "--git-dir"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def setup_repo():
    """Initialize Git repo if needed"""
    if not verify_git_repo():
        print("Initializing new Git repository...")
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "config", "user.name", USER_NAME], check=True)
        subprocess.run(["git", "config", "user.email", USER_EMAIL], check=True)
    else:
        print("Existing Git repository found")

def create_project_files():
    """Create initial project structure"""
    dirs = [
        "terraform/aws",
        "terraform/gcp",
        "terraform/azure",
        "kubernetes/manifests",
        "scripts"
    ]
    
    for d in dirs:
        os.makedirs(os.path.join(REPO_DIR, d), exist_ok=True)
    
    # Create sample files
    with open(os.path.join(REPO_DIR, "terraform/aws/main.tf"), "w") as f:
        f.write("# AWS EKS Configuration\n")
    
    with open(os.path.join(REPO_DIR, "kubernetes/manifests/deployment.yml"), "w") as f:
        f.write("---\n# Kubernetes Deployment\n")

def make_commit(commit_date, message):
    """Make a commit with specific date"""
    env = os.environ.copy()
    date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    subprocess.run(["git", "add", "-A"], check=True, env=env)
    subprocess.run(["git", "commit", "-m", message], check=True, env=env)
    print(f"Created commit: {commit_date.strftime('%Y-%m-%d')} - {message}")

def generate_commits():
    """Generate 50 realistic commits"""
    start_date = datetime(2024, 7, 1)
    end_date = datetime(2024, 9, 30)
    
    for i in range(1, 51):
        # Random date in range
        days_diff = random.randint(0, (end_date - start_date).days)
        commit_date = start_date + timedelta(days=days_diff)
        
        # Modify random file
        file_choices = [
            "terraform/aws/main.tf",
            "kubernetes/manifests/deployment.yml",
            f"scripts/update_{i}.sh"
        ]
        file_to_modify = random.choice(file_choices)
        
        with open(os.path.join(REPO_DIR, file_to_modify), "a") as f:
            f.write(f"\n# Update {i} - {datetime.now()}")
        
        # Commit with DevOps message
        messages = [
            "Updated infrastructure code",
            "Fixed deployment issue",
            "Added new cluster config",
            "Optimized resource allocation",
            "Updated security policies"
        ]
        msg = f"{random.choice(messages)} (commit {i})"
        
        make_commit(commit_date, msg)

def main():
    print(f"Working in directory: {REPO_DIR}")
    os.chdir(REPO_DIR)
    
    setup_repo()
    create_project_files()
    generate_commits()
    
    print("\nDone! Verify commits with:")
    print("git log --oneline --graph --all")
    print("\nTo push to GitHub when ready:")
    print("git remote add origin YOUR_REPO_URL")
    print("git push -u origin main")

if __name__ == "__main__":
    main()
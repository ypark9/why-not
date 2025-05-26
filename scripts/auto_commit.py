import os
import git
from github import Github
from datetime import datetime
import logging
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv('GITHUB_ACCESS_TOKEN') or os.getenv('ACCESS_TOKEN')

if not access_token:
    raise ValueError("GitHub Access Token not found. Please set it in the GitHub Actions secrets or the .env file.")

if 'GITHUB_ACTIONS' in os.environ:
    local_dir = '/home/runner/work/why-not/why-not'
else:
    local_dir = '/Users/yoonsoo.park/code/auto-commit-and-chill'

repo_name = 'ypark9/why-not'
file_name = 'ypark9-magic.txt'
commit_message = 'Auto-update: Why not commit? 🚀'
branch_name = 'main'

file_content = f"This file was created or updated on {datetime.now()}"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create_or_update_file(file_path, content):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        logger.info(f"File '{file_path}' created/updated successfully.")
    except Exception as e:
        logger.error(f"Error writing to file '{file_path}': {e}")
        raise

def commit_and_push_changes(repo, file_path, commit_message, branch_name):
    try:
        repo.index.add([file_path])
        repo.index.commit(commit_message)
        logger.info(f"Committed changes: '{commit_message}'")
        
        origin = repo.remotes.origin
        origin.push(refspec=f'{branch_name}:{branch_name}')
        logger.info(f"Changes pushed to branch '{branch_name}' successfully.")
    except Exception as e:
        logger.error(f"Error during commit or push: {e}")
        raise

def main():
    try:
        repo = git.Repo(local_dir)

        if branch_name not in [branch.name for branch in repo.branches]:
            logger.info(f"Branch '{branch_name}' does not exist locally. Creating it...")
            repo.git.checkout('-b', branch_name)
        else:
            repo.git.checkout(branch_name)

        new_file_path = os.path.join(local_dir, file_name)

        if os.path.exists(new_file_path):
            logger.info(f"File '{file_name}' already exists. It will be updated.")
        else:
            logger.info(f"File '{file_name}' does not exist. It will be created.")

        create_or_update_file(new_file_path, file_content)

        repo.git.config('user.name', 'ypark9')  # Name
        repo.git.config('user.email', 'yoonsoo@duck.com')  # Email

        commit_and_push_changes(repo, new_file_path, commit_message, branch_name)

        g = Github(access_token)
        repo_github = g.get_repo(repo_name)

        commits = repo_github.get_commits(sha=branch_name)
        logger.info(f"Latest commit on branch '{branch_name}': {commits[0].commit.message}")

    except git.exc.InvalidGitRepositoryError:
        logger.error("Invalid Git repository. Please check the local directory.")
    except git.exc.GitCommandError as e:
        logger.error(f"Git command error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()

import os
import git
from github import Github
from datetime import datetime
import logging
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv('GITHUB_TOKEN')  # Token from GitHub Actions secret

if not access_token:
    raise ValueError("GitHub Access Token not found. Please set it in the GitHub Actions secrets.")

if 'GITHUB_ACTIONS' in os.environ:
    local_dir = '/home/runner/work/auto-commit-and-chill/auto-commit-and-chill'  # Runner path
else:
    local_dir = '/home/anil/Desktop/learning/learn-scripting/auto-commit-and-chill'  # Local path

repo_name = 'anilrajrimal1/auto-commit-and-chill'
file_name = 'anil-magic.txt'
commit_message = 'Update example file using Python script'
branch_name = 'master'

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

def commit_and_push_changes(repo, file_path, commit_message, branch_name, token):
    try:
        # Stage the file for commit
        repo.index.add([file_path])

        # Commit the changes
        repo.index.commit(commit_message)
        logger.info(f"Committed changes: '{commit_message}'")

        # Configure the Git credentials using the token
        repo.git.config('user.name', 'GitHub Actions')  # Set user name
        repo.git.config('user.email', 'github-actions@github.com')  # Set user email

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
            logger.error(f"Branch '{branch_name}' does not exist locally. Please create or checkout the branch.")
            return

        repo.git.checkout(branch_name)

        new_file_path = os.path.join(local_dir, file_name)

        if os.path.exists(new_file_path):
            logger.info(f"File '{file_name}' already exists. It will be updated.")
        else:
            logger.info(f"File '{file_name}' does not exist. It will be created.")

        create_or_update_file(new_file_path, file_content)

        commit_and_push_changes(repo, new_file_path, commit_message, branch_name, access_token)

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

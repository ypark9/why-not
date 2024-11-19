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

# Configuration
repo_name = 'anilrajrimal1/auto-commit-and-chill'  # Repo
local_dir = '/home/anil/Desktop/learning/learn-scripting/auto-commit-and-chill'  # Local path
file_name = 'anil-magic.txt'  # File
commit_message = 'Update example file using Python script'  # Commit message
branch_name = 'master'  # Branch name to push changes

file_content = f"This file was created or updated on {datetime.now()}"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create_or_update_file(file_path, content):
    """
    Create a new file or update the existing file with the given content.
    """
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        logger.info(f"File '{file_path}' created/updated successfully.")
    except Exception as e:
        logger.error(f"Error writing to file '{file_path}': {e}")
        raise

def commit_and_push_changes(repo, file_path, commit_message, branch_name):
    """
    Commit and push the changes to the specified branch.
    """
    try:
        # Stage the file for commit
        repo.index.add([file_path])

        # Commit the changes
        repo.index.commit(commit_message)
        logger.info(f"Committed changes: '{commit_message}'")

        # Push the changes to the remote repository
        origin = repo.remotes.origin
        origin.push(refspec=f'{branch_name}:{branch_name}')
        logger.info(f"Changes pushed to branch '{branch_name}' successfully.")

    except Exception as e:
        logger.error(f"Error during commit or push: {e}")
        raise

def main():
    try:
        # Initialize the local Git repository
        repo = git.Repo(local_dir)

        # Check if the branch exists locally
        if branch_name not in [branch.name for branch in repo.branches]:
            logger.error(f"Branch '{branch_name}' does not exist locally. Please create or checkout the branch.")
            return

        # Switch to the specified branch
        repo.git.checkout(branch_name)

        # Define the full path of the file to create/update
        new_file_path = os.path.join(local_dir, file_name)

        # Check if the file exists in the repository
        if os.path.exists(new_file_path):
            logger.info(f"File '{file_name}' already exists. It will be updated.")
        else:
            logger.info(f"File '{file_name}' does not exist. It will be created.")

        # Create or update the file with new content
        create_or_update_file(new_file_path, file_content)

        # Commit and push the changes
        commit_and_push_changes(repo, new_file_path, commit_message, branch_name)

        # Connect to GitHub and verify the commit
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

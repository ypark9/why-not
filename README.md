
# Auto Commit and Chill

Welcome to **Auto Commit and Chill**, the coolest way to automate your GitHub commits like a boss! 🚀

## Table of Contents  
- [What is it?](#what-is-it)  
- [Features](#features)  
- [How Does It Work?](#how-does-it-work)  
- [Getting Started](#getting-started)  
  - [Clone the Repository](#clone-the-repository)  
  - [Set Up Your GitHub](#set-up-your-github)  
  - [Update the Script](#update-the-script)  
  - [Add GitHub Token and SSH Key](#add-github-token-and-ssh-key)  
  - [Configure Workflow](#configure-workflow)  
- [Schedule](#schedule)  
- [Why Should You Use This?](#why-should-you-use-this)  
- [License](#license)  

## What is it?  
This project automatically commits and pushes changes to your GitHub repository, so you can focus on the fun stuff and leave the repetitive tasks to the robots. 🤖💻  

## Features:  
- Automatic commits every 2 hours (because, why not?) ⏰  
- Pushes changes directly to your repo. No more "manual" pushing. It's like magic, but real. ✨  
- Works seamlessly on GitHub Actions (and locally too, if you prefer to live dangerously). 🏠  

## How Does It Work?  
1. Create or update a file (I'm using `anil-magic.txt` for example – because it’s magic).  
2. Commit and push those changes to your GitHub repo. 🏆  
3. All automated. No humans involved (except when setting it up, obviously). 😎  

## Getting Started  

### Clone the Repository  
Clone the project repository using SSH:  
```bash  
git clone git@github.com:anilrajrimal1/auto-commit-and-chill.git  
```  

### Set Up Your GitHub  
1. Create a new repository on your GitHub account.  
2. Set the newly created repository as the upstream:  
   ```bash  
   git remote add upstream <your-repo-url>  
   ```  

### Update the Script  
Modify the following variables in the script:  
```python  
if 'GITHUB_ACTIONS' in os.environ:  
    local_dir = '/home/runner/work/auto-commit-and-chill/auto-commit-and-chill'  
else:  
    local_dir = '/home/anil/Desktop/learning/learn-scripting/auto-commit-and-chill'  

repo_name = '<your-username>/<your-repo>'  
file_name = 'anil-magic.txt'  
commit_message = 'Update example file using Python script'  
branch_name = 'master'  

repo.git.config('user.name', '<your-username>')  # Name  
repo.git.config('user.email', '<your-email>')  # Email  
```  

### Add GitHub Token and SSH Key  
1. Generate a **GitHub Access Token** with `repo` and `workflow` permissions.  
2. Add the token to your `.env` file and as a GitHub secret in your repository with the title `ACCESS_TOKEN`
3. Generate or use an existing SSH key pair associated with your GitHub account. 
4. If you already had the pair, add the public key to your GitHub account and associated private key as a GitHub secret with the title `ACTIONS_SSH_KEY`.

### Configure Workflow  
Uncomment the following trigger in the workflow configuration file (`.github/workflows/main.yml`):  
```yaml  
on:  
  # schedule:  
  #   - cron: '0 */2 * * *' # Every 2 hours  
  workflow_dispatch:  
```  

Push the codebase to the upstream repository forcefully:  
```bash  
git push -u upstream master --force  
```  

## Schedule  
- The workflow runs automatically every 2 hours.  
- You can also manually trigger it via the GitHub Actions UI.  

## Why Should You Use This?  
- **Procrastination level**: Expert 🏆  
- **Productivity level**: 1000% 📈  
- **Stress level**: Zero 👌  

Just sit back, relax, and let this little script handle the rest. 😎  

## License  
This project is licensed under the [MIT License](LICENSE), so feel free to use it, share it, or even improve it if you’re in the mood. 🎉  

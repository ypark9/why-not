# Setup Guide for ypark9/why-not

## 🚀 Complete Setup Instructions

### Prerequisites

- GitHub account: `ypark9`
- Email: `yoonsoo@duck.com`
- Target repository: `ypark9/why-not`

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository named `why-not`
3. Make it public (recommended for this demo)
4. Initialize with a README if you want

### Step 2: Generate GitHub Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name like "Auto Commit Bot"
4. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
5. Click "Generate token" and **copy the token immediately**

### Step 3: Set Up Repository Secrets

1. Go to your `ypark9/why-not` repository
2. Settings → Secrets and variables → Actions
3. Add one secret:
   - **Name**: `ACCESS_TOKEN` **Value**: Your GitHub token from Step 2

### Step 4: Push Code to Your Repository

```bash
# If you already have this project locally (you're already here!)
# Just add your repository as the new origin
git remote remove origin
git remote add origin https://github.com/ypark9/why-not.git

# Push to your repository
git push -u origin main --force
```

**Alternative - Fresh Clone:**

```bash
# Clone this project locally
git clone https://github.com/anilrajrimal1/auto-commit-and-chill.git
cd auto-commit-and-chill

# Add your repository as the new origin
git remote remove origin
git remote add origin https://github.com/ypark9/why-not.git

# Push to your repository
git push -u origin main --force
```

### Step 5: Enable Automatic Schedule (Optional)

To enable the 2-hour automatic commits, edit `.github/workflows/magic-script.yml`:

```yaml
on:
  schedule:
    - cron: "0 */2 * * *" # Every 2 hours
  workflow_dispatch:
```

### Step 6: Test the Setup

1. Go to your repository on GitHub
2. Actions tab → "Auto Commit and Push" workflow
3. Click "Run workflow" → "Run workflow"
4. Watch it execute!

### What Happens When It Runs?

- Creates/updates `ypark9-magic.txt` with current timestamp
- Commits with message: "Auto-update: Why not commit? 🚀"
- Pushes to your `main` branch
- Runs every 2 hours (if scheduled) or manually

### Local Development

1. Create a `.env` file:

```bash
cp .env.example .env
```

2. Add your GitHub token to `.env`:

```env
GITHUB_ACCESS_TOKEN=your_actual_token_here
```

3. Run locally:

```bash
pip install -r requirements.txt
python scripts/auto_commit.py
```

## 🎉 You're All Set!

Your "Why Not" auto-commit project is ready to rock! 🚀

### Troubleshooting

- **Permission denied**: Check your GitHub token has the right permissions (`repo` and `workflow`)
- **Token errors**: Verify your `ACCESS_TOKEN` secret is set correctly in repository settings
- **Branch errors**: Make sure you're using `main` branch (not `master`)
- **Authentication failed**: If pushing locally fails, you may need to use a Personal Access Token instead of password
- **Remote already exists**: Run `git remote remove origin` then `git remote add origin https://github.com/ypark9/why-not.git`

### Local Git Authentication

If you're pushing locally and get authentication errors, you have two options:

**Option 1: Use token in URL (easier)**

```bash
git remote set-url origin https://TOKEN@github.com/ypark9/why-not.git
```

**Option 2: Configure Git credentials**

```bash
git config credential.helper store
# Then on first push, enter your GitHub username and use your token as password
```

Need help? The automation should work seamlessly once these steps are complete!

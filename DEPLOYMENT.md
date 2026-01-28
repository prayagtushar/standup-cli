# Deployment Guide for standup-cli

This guide explains how to deploy and release standup-cli to different package managers.

## 1. PyPI (Python Package Index)

### Automated Release (Recommended)

The project uses GitHub Actions to automatically publish to PyPI when you create a version tag.

**Steps:**

1. **Create a PyPI Account** (if you don't have one)
   - Visit https://pypi.org/account/register/
   - Verify your email
   - Create an API token at https://pypi.org/manage/account/token/

2. **Add PyPI Token to GitHub Secrets**
   - Go to your GitHub repo → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI API token

3. **Tag a Release**
   ```bash
   git tag -a v0.1.0 -m "Release version 0.1.0"
   git push origin v0.1.0
   ```

4. **Watch the Workflow**
   - Go to GitHub Actions tab
   - The "Publish to PyPI" workflow will automatically run
   - Check PyPI after workflow completes

### Manual Release

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Upload to PyPI
twine upload dist/*
```

## 2. GitHub Releases

The workflow automatically creates a GitHub Release with build artifacts.

**Manual Release:**
```bash
# Create a tag
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0

# The workflow will automatically create a release
# Or manually create one at: https://github.com/prayagtushar/standup-cli/releases/new
```

**Installation from GitHub:**
```bash
pip install git+https://github.com/prayagtushar/standup-cli.git
```

## 3. Homebrew

### Submit to Homebrew Core (Public Official Formula)

1. **Generate SHA256 of Your PyPI Release**
   ```bash
   # After publishing to PyPI, download and get SHA256
   pip download standup-cli==0.1.0 --no-deps
   sha256sum standup-cli-0.1.0.tar.gz
   ```

2. **Update `standup-cli.rb`**
   - Update the `url` to your PyPI release
   - Update the `sha256` hash

3. **Create a Fork of Homebrew Core**
   - Fork https://github.com/Homebrew/homebrew-core

4. **Create a New Branch**
   ```bash
   git checkout -b standup-cli
   ```

5. **Add Formula to Homebrew**
   ```bash
   # Create a new file
   cp standup-cli.rb homebrew-core/Formula/s/standup-cli.rb
   ```

6. **Test Locally**
   ```bash
   brew install --build-from-source Formula/s/standup-cli.rb
   standup-cli --help
   ```

7. **Submit Pull Request**
   - Push to your fork
   - Create PR to Homebrew/homebrew-core
   - Include description and testing confirmation

### Tap (Custom Homebrew Repository - Quicker Alternative)

Create your own Homebrew tap for faster distribution:

```bash
# Create a tap repository
git clone https://github.com/prayagtushar/homebrew-standup-cli.git

# Add formula
mkdir -p Formula
cp standup-cli.rb Formula/

# Commit and push
git add Formula/standup-cli.rb
git commit -m "Add standup-cli formula"
git push
```

**Users install with:**
```bash
brew tap prayagtushar/standup-cli
brew install standup-cli
```

## Installation Methods for Users

### From PyPI (Recommended for Python developers)
```bash
pip install standup-cli
standup-cli
```

### From GitHub
```bash
pip install git+https://github.com/prayagtushar/standup-cli.git
standup-cli
```

### From Homebrew (macOS)
```bash
# Once published to Homebrew Core
brew install standup-cli

# Or from a custom tap
brew tap prayagtushar/standup-cli
brew install standup-cli
```

## Version Bumping

When releasing a new version:

1. **Update version in `setup.py` and `pyproject.toml`**
2. **Create a git tag**
   ```bash
   git tag -a v0.2.0 -m "Release version 0.2.0"
   git push origin v0.2.0
   ```
3. **Update Homebrew formula with new SHA256** (if using a tap)

## Troubleshooting

- **PyPI Upload Fails**: Check token permissions at https://pypi.org/manage/account/token/
- **Homebrew Formula Error**: Test with `brew audit --strict Formula/s/standup-cli.rb`
- **SHA256 Mismatch**: Regenerate by downloading from PyPI and running `sha256sum`

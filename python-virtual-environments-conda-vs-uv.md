# Python Virtual Environment Management: conda vs uv

## Table of Contents
- [Key Concepts](#key-concepts)
- [Python Version Management](#python-version-management)
- [Non-Python Packages](#non-python-packages-key-difference)
- [Common Command Comparison](#common-command-comparison)
- [When to Use What](#when-to-use-what)
- [Installation Notes](#important-installation-notes)
- [Key Lessons](#key-lessons-from-experience)
- [Quick Start Guide](#quick-start-with-uv)

---

## Key Concepts

uv 在国内使用最主要两个环境变量

1. 安装 uv `UV_INSTALLER_GITHUB_BASE_URL`

```
export UV_INSTALLER_GITHUB_BASE_URL="https://gh-proxy.com/https://github.com"
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. 安装 python 版本  `UV_PYTHON_INSTALL_MIRROR`

```
export UV_PYTHON_INSTALL_MIRROR="https://gh-proxy.com/https://github.com/astral-sh/python-build-standalone/releases/download"
uv python install 3.11
```



### Virtual Environment Philosophy

**conda**: Centralized, named environments
- One environment (e.g., `ml_projects`) shared across multiple projects
- Located in `~/miniconda3/envs/`
- Activate from anywhere: `conda activate ml_projects`

**uv**: Decentralized, per-project environments
- Each project has its own `.venv/` directory
- Located inside project: `~/projects/my_project/.venv/`
- Activate from project directory: `source .venv/bin/activate`

### Disk Space Comparison

| Aspect | conda | uv |
|--------|-------|-----|
| **Environment size** | 3-5GB each | 1-3GB each |
| **Shared environments** | One copy for multiple projects | Each project has own copy |
| **Cache efficiency** | Less efficient | Smart caching, hardlinks |
| **Total for 5 projects** | 5GB (1 shared env) | 8-10GB (5 separate envs) |
| | OR 15-25GB (5 separate envs) | But with cache: ~4-6GB actual |

### Installation Speed

| Tool | Speed | Typical Time |
|------|-------|--------------|
| **conda** | Slow | 2-5 minutes |
| **uv** | Very fast | 10-30 seconds |
| **pip** | Medium | 1-3 minutes |

**Speedup: uv is 10-100x faster than conda/pip**

---

## Python Version Management

### Comparison Table

| Tool | Can Install Python? | Method | Notes |
|------|---------------------|--------|-------|
| **conda** | ✅ Built-in | `conda create -n env python=3.10` | Downloads pre-built Python |
| **uv** | ✅ Built-in | `uv python install 3.10` | Downloads pre-built Python (fast) |
| **pyenv** | ✅ Compiles | `pyenv install 3.10.12` | Compiles from source (slow but customizable) |
| **venv** | ❌ No | `python3.10 -m venv env` | Uses existing system Python |
| **poetry** | ❌ No | Via pyenv | Requires pyenv for version management |
| **pipenv** | ❌ No | Via pyenv | Requires pyenv for version management |

### Recommended Combinations

**For conda users:**
```bash
# Conda handles everything
conda create -n myenv python=3.10
conda activate myenv
conda install packages
```

**For uv users:**
```bash
# Option 1: uv for Python + packages
uv python install 3.10
uv venv --python 3.10
uv pip install packages

# Option 2: pyenv + uv (more control)
pyenv install 3.10.12
pyenv local 3.10.12
uv venv  # Auto-detects pyenv's Python
uv pip install packages
```

---

## Non-Python Packages (Key Difference)

### What conda CAN Install (uv/pip CANNOT)

**System binaries:**
```bash
conda install ffmpeg imagemagick graphviz
```

**CUDA toolkit and libraries:**
```bash
conda install cudatoolkit cudnn
```

**Other languages:**
```bash
conda install r-base r-essentials julia
```

**System libraries:**
```bash
conda install openssl sqlite zlib libstdcxx
```

### What uv/pip CAN Install

**Only Python packages:**
- Python libraries (.py files)
- Python packages with compiled extensions (.so, .pyd files)
- But extensions must be pre-compiled (wheels) or build tools must be available

### For System Tools, Use:

**Linux:**
```bash
sudo apt install ffmpeg cmake ninja-build
```

**macOS:**
```bash
brew install ffmpeg cmake ninja
```

**Windows:**
```bash
choco install ffmpeg cmake ninja
```

**Or use conda** (if no sudo access):
```bash
conda install ffmpeg cmake ninja
```

### Hybrid Approach (Recommended)

```bash
# System tools via conda (or apt/brew)
conda install ffmpeg

# Python packages via uv
cd ~/project
uv venv --python 3.10
source .venv/bin/activate
uv pip install vllm xinference pytorch

# Both work together harmoniously
# But need to set LD_LIBRARY_PATH if using conda libraries:
export LD_LIBRARY_PATH=/home/user/miniconda3/lib:$LD_LIBRARY_PATH
```

---

## Common Command Comparison

| Task | conda | uv |
|------|-------|-----|
| **Create environment** | `conda create -n myenv python=3.10` | `cd project && uv venv --python 3.10` |
| **Activate** | `conda activate myenv` | `source .venv/bin/activate` |
| **Deactivate** | `conda deactivate` | `deactivate` |
| **Install package** | `conda install package` | `uv pip install package` |
| | `pip install package` | |
| **Install specific version** | `conda install package=1.2.3` | `uv pip install package==1.2.3` |
| **Install from requirements** | `conda install --file requirements.txt` | `uv pip install -r requirements.txt` |
| **Upgrade package** | `conda update package` | `uv pip install -U package` |
| **List packages** | `conda list` | `uv pip list` |
| **Show package info** | `conda list package` | `uv pip show package` |
| **Export environment** | `conda env export > env.yml` | `uv pip freeze > requirements.txt` |
| **Create from file** | `conda env create -f env.yml` | `uv pip install -r requirements.txt` |
| **Remove environment** | `conda env remove -n myenv` | `rm -rf .venv` |
| **List environments** | `conda env list` | `find ~ -type d -name ".venv"` |
| **Clean cache** | `conda clean --all` | `uv cache clean` |

### Special Notes

**Installing PyTorch with CUDA:**

```bash
# conda
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch

# uv (recommended for PyTorch)
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**Working in activated environment:**

Both conda and uv environments work the same once activated:
```bash
# After activation, these work identically
python script.py
pip install package  # (or uv pip install package)
which python  # Shows environment's Python
```

---

## When to Use What

### Use conda when:

✅ **Need non-Python packages**
- ffmpeg, graphviz, cmake, CUDA toolkit
- R, Julia, system libraries

✅ **Multiple similar projects share environment**
- All ML projects use same stack
- Disk space savings with shared environment

✅ **Already familiar with conda**
- Team uses conda
- Existing conda workflows

✅ **HPC/cluster without root access**
- Can't use apt/yum to install system packages
- Need isolated userspace installations

✅ **Need optimized numerical libraries**
- MKL-optimized NumPy/SciPy (10-20% faster)
- Intel CPU optimizations

### Use uv when:

✅ **Projects have different dependency versions**
- Project A: vLLM 0.5.1
- Project B: vLLM 0.6.0
- Need complete isolation

✅ **Need faster installs**
- 10-100x speedup over conda/pip
- Frequent package installations

✅ **Want smaller disk footprint**
- Environments 40-60% smaller than conda
- Smart caching across projects

✅ **Deploying to production**
- Docker containers (pip/uv is standard)
- Cloud servers
- requirements.txt is universal

✅ **Team collaboration**
- requirements.txt is industry standard
- Better version control integration
- CI/CD pipelines expect pip

✅ **Modern LLM/AI projects**
- vLLM, Xinference, TGI use pip
- Community expects pip workflows
- Documentation uses pip examples

### Hybrid Approach (Best of Both)

**Recommended for ML/AI work:**

```bash
# System tools via conda
conda install ffmpeg "ffmpeg<8"

# Python version via pyenv or uv
uv python install 3.10

# Python packages via uv (per-project)
cd ~/project1
uv venv --python 3.10
source .venv/bin/activate
uv pip install vllm xinference

cd ~/project2
uv venv --python 3.11
source .venv/bin/activate
uv pip install transformers datasets
```

**Benefits:**
- Conda: Manages system dependencies
- uv: Fast Python package management
- Each for what it does best

---

## Important Installation Notes

### Installing uv Correctly

**Two valid methods:**

**Method 1: System-wide installation (Recommended)**
```bash
# Install uv system-wide (outside conda)
ubuntu@VM-4-138-ubuntu:~$ export UV_INSTALLER_GITHUB_BASE_URL="https://gh-proxy.com/https://github.com"
ubuntu@VM-4-138-ubuntu:~$ curl -LsSf https://astral.sh/uv/install.sh | sh

# Installs to ~/.local/bin/uv
# Add to PATH
export PATH="$HOME/.local/bin:$PATH"

# Make permanent
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify
which uv
# Should show: /home/user/.local/bin/uv
```

**Why recommended:**
- Available outside conda environments
- Faster startup (no conda overhead)
- Standard installation method

**Method 2: Via pip in conda base (Also works)**
```bash
# This actually works fine!
conda activate base
pip install uv

# Verify
which uv
# Shows: /home/user/miniconda3/bin/uv
```

**Why this works:**
- `uv` is smart enough to detect active venvs
- `uv pip install` installs to the correct location (your .venv)
- We verified this works correctly in practice

**Trade-offs:**
- ✅ Simpler if you already use conda
- ✅ `uv` commands work correctly with venvs
- ❌ Only available when conda is in PATH
- ❌ Slightly slower startup (loads conda environment)

**Our testing showed:** Both methods work! The system-wide install is recommended for consistency, but installing via pip in conda base also functions correctly.

### Setting Up LD_LIBRARY_PATH (If Using Conda Libraries)

If you use conda for system tools (like ffmpeg) but uv for Python packages:

```bash
# Add to ~/.bashrc
export LD_LIBRARY_PATH=/home/user/miniconda3/lib:$LD_LIBRARY_PATH

# Reload
source ~/.bashrc
```

This makes conda's shared libraries (`.so` files) available to uv environments.

---

## Key Lessons from Experience

### 1. Always Specify Python Version Explicitly

**❌ Bad:**
```bash
uv venv  # Which Python will it use?
```

**✅ Good:**
```bash
uv venv --python 3.11  # Explicit, clear
```

**Why:** Without `--python`, uv uses whatever Python is in PATH (might be conda's, system's, or uv's).

### 2. Use `uv pip`, Not `pip` in uv Environments

**In activated uv venv:**
```bash
# Check which pip
which pip
# Might show: /home/user/miniconda3/bin/pip (conda's pip!)

# Check which uv pip uses
uv pip --version
# Uses venv's Python correctly

# Therefore, use:
uv pip install package  # ✅ Correct
# NOT:
pip install package  # ❌ Might go to wrong location
```

**Or use:**
```bash
python -m pip install package  # Also correct
```

### 3. Set LD_LIBRARY_PATH for Conda Libraries

If using conda's ffmpeg with uv's Python packages:

```bash
export LD_LIBRARY_PATH=/home/user/miniconda3/lib:$LD_LIBRARY_PATH

# Test
python -c "import ctypes; ctypes.CDLL('/path/to/conda/lib/libavutil.so')"
```

### 4. Re-activate venv in tmux

**Problem:**
```bash
# Outside tmux
source .venv/bin/activate
(.venv) $ tmux

# Inside tmux - venv NOT active!
$ which python
/usr/bin/python  # System Python!
```

**Solution:**
```bash
# Inside tmux, re-activate
source .venv/bin/activate
```

### 5. Conda and uv Can Coexist

You can have both installed and use each for its strengths:

```bash
# conda for system tools
conda install ffmpeg cmake

# uv for Python packages (even with uv installed via conda!)
uv venv --python 3.10
uv pip install pytorch transformers
```

**Important clarification:** Installing `uv` via `pip install uv` in conda base works fine! We initially thought this caused issues, but testing proved:
- `uv pip install` correctly installs to `.venv` (not conda)
- `uv venv` creates proper isolated environments
- The F5-TTS issue was **torchcodec version incompatibility**, not uv installation method

**The real lesson:** `uv` installed via conda or system-wide both work. System-wide is recommended for consistency, but conda installation is functional.

### 6. Venv Naming Convention (uv)

uv uses **parent directory name** as venv name in prompt:

```bash
cd ~/my-awesome-project
uv venv
source .venv/bin/activate

# Prompt shows:
(my-awesome-project) $
# Not (venv) or (.venv)
```

**Name your directories descriptively!**

---

## Quick Start with uv

### One-Time Setup

```bash
# 1. Install uv system-wide
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# 2. Make PATH permanent
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# 3. Install Python versions you need
uv python install 3.10
uv python install 3.11

# 4. Verify
uv --version
uv python list
```

### Per-Project Usage

```bash
# Navigate to project
cd ~/projects/my_project

# Create venv
uv venv --python 3.10

# Activate
source .venv/bin/activate

# Install packages
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
uv pip install transformers datasets accelerate

# Save dependencies
uv pip freeze > requirements.txt

# Deactivate when done
deactivate
```

### Recreating Environment on Another Machine

```bash
# On new machine
cd ~/projects/my_project

# Install uv if not present
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create venv
uv venv --python 3.10
source .venv/bin/activate

# Install from requirements
uv pip install -r requirements.txt

# Done!
```

### Common Workflows

**Starting work on existing project:**
```bash
cd ~/projects/my_project
source .venv/bin/activate
# Work...
deactivate
```

**Adding new dependency:**
```bash
cd ~/projects/my_project
source .venv/bin/activate
uv pip install new-package
uv pip freeze > requirements.txt  # Update requirements
git add requirements.txt
git commit -m "Add new-package"
```

**Upgrading packages:**
```bash
source .venv/bin/activate
uv pip install -U package-name
# Or upgrade all:
uv pip install -U -r requirements.txt
```

**Cleaning up:**
```bash
# Remove venv
rm -rf .venv

# Recreate fresh
uv venv --python 3.10
source .venv/bin/activate
uv pip install -r requirements.txt
```

---

## Decision Matrix

| Your Situation | Recommendation |
|----------------|----------------|
| Solo developer, experimenting | Either works (conda simpler) |
| Team project, version control | uv (requirements.txt standard) |
| Need ffmpeg, R, system tools | conda or hybrid |
| Pure Python, modern ML (vLLM, etc) | uv |
| Multiple projects, different versions | uv (better isolation) |
| Disk space limited | uv (smaller environments) |
| Speed matters (frequent installs) | uv (10-100x faster) |
| Already using conda, comfortable | Stay with conda |
| Learning modern Python practices | Learn uv |
| HPC cluster, no root access | conda (can install system tools) |
| Docker/cloud deployment | uv (standard in containers) |

---

## Additional Resources

**uv Documentation:**
- Official docs: https://docs.astral.sh/uv/
- GitHub: https://github.com/astral-sh/uv

**conda Documentation:**
- Official docs: https://docs.conda.io/
- Miniforge (lightweight): https://github.com/conda-forge/miniforge

**pyenv:**
- GitHub: https://github.com/pyenv/pyenv

**Best Practices:**
- Always use virtual environments (never install globally)
- Pin dependency versions in production
- Use lock files for reproducibility
- Document which tool you're using in README

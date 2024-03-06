# simple-updater

A simple updater for git repositories on a server using GitHub actions.

## Usage

1. Install flask

```bash
pip install flask
```

2. Modify the `UPDATER_TOKEN` constant in `updater.py`

3. Run the server

```bash
python updater.py
```

4. Create a workflow file and add a secret to your repository

```yaml
name: Update
on:
  push:
    branches:
      - main
jobs:
  update:
    runs-on: ubuntu-latest

    steps:
      - name: Update
        run: curl https://[your_server]/update?repo=[repo_name]&token=${{ secrets.UPDATE_TOKEN }}
```

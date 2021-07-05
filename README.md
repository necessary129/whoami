# whoami

An easy way for you to publish your identities signed with GPG.

Pins time of update with latest bitcoin blockhash and automatically snapshots the page with [Internet Archive](https://web.archive.org/).

## Setup

First fork this repo. And git clone the fork. Activate Github pages (with branch `gh-pages`) and Github Actions on your fork.

Then setup a venv:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install -U requirements.txt
```

Copy the `pre-commit` hook to `.git/hooks`:

```
cp pre-commit .git/hooks/
```

Edit `identities/conf.yaml` to add whatever identities you want (Be sure to change the urls too), and edit `identities/misc/` to add any arbitrary content.

`misc` follows the structure:

```
misc/
	<directory>/
		title
		content.md
```

Git commit (preferably a GPG signed commit), push, And you are good to go!

#### NOTE: Always enable your virtualenv with `source .venv/bin/activate` before doing anything

#### Also NOTE: Internet Archive only creates a new snapshot when the previous snapshot is older than 45 minutes. So be careful not to update your identities without atleast 45 minutes in between. Otherwise some changes may not be snapshotted.

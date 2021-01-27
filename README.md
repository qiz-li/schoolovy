<img src="icon.png" width= 130px align="right" />

# Schoolovy
> Auto-like Schoology posts & comments

Share some love using this Python script to automatically like *all posts & comments* in your [Schoology](https://www.schoology.com/) feed (most recent 20 posts).

## Installation
Clone from GitHub:

```bash
git clone https://github.com/N-l1/schoolovy.git
```

```bash
cd schoolovy
```

Install required Python libraries:

```bash
pip install -r requirements.txt
```
## Configuration
Retreive your API key and secret from ``https://[school_url].com/api`` (e.g. ``https://harvard.schoology.com/api``) and add the ID & secret to the ``config.yaml`` included in the repository.

**Mac**:
```bash
open config.yaml
```
**Windows**:
```powershell
Notepad config.yaml
```
## Run
Make sure you have ```>= Python 3.6``` installed, then run the script with:

```bash
python3 schoolovy.py
```

The script should now indicate it has started by outputting:

```
Sharing love...
Liked 7 new posts
```

All posts in your feed should now be liked! You can like all new posts & comments by setting up a cron job to do this continuously.

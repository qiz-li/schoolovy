<img src="icon.png" width= 150px align="right" />

# Schoolovy

> A Schoology auto-liker

Use this Python script to automatically like
posts & comments in your [Schoology](https://www.schoology.com/) feed.

## Install

Clone from GitHub:

```bash
git clone https://github.com/qiz-li/schoolovy.git
```

```bash
cd schoolovy
```

Install required Python dependencies:

```bash
pip3 install -r requirements.txt
```

## Configure

Open the `config.yaml` file and
change the example key and secret to ones tied to your account.
You can find them at `{school_schoology_url}.com/api`.

## Run

Make sure you have >= Python 3.6 installed, then run the script with:

You can change the argument to the number of posts you want the script to check for.
In this case, the script will check the most recent 20 posts.
Out of the specified posts, ones that are not already liked will be auto-liked.

```bash
python3 schoolovy.py 20
```

The script should now indicate it has started by outputting:

```
Liking posts...
---------------
Liked 5 posts and 2 comments
```

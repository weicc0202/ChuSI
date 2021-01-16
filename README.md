# ChuCI

ChuSI is a Self-Introduction robot using LINE Message API to help to introduce your self

## Getting started

### Deploy to heroku
heroku create chusi
heroku git:remote -a chusi
heroku config:set LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
heroku config:set LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN

```
$ export LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
$ export LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN

$ pip install -r requirements.txt
```

Run WebhookParser sample

```
$ python app.py
```

Run WebhookHandler sample

```
$ python app_with_handler.py
```
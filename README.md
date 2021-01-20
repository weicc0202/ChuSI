

ChuSI 
==================================================================================================
> An chatbot to introduce yourself by understanding your resume.


## Version 0.2.0

<img align="right" src="https://imgur.com/Jr8YwzM.gif?row=true" height="440">

**For version 0.2.0, ChuSI is only tested on iOS devices**
> In the other words, messages may not be shown noramlly on the chrome/desktop version of LINE.

Therefore, to have the **best experience** for this application, it is recommended to enjoy ChuSI on your mobile phone.

- New features:
	- Static Recommendation for next section.
	- Combine AWS DynamoDB to store information.
	- Add more attractive welcome messages!
	- Modify interface for using `agent.py` and `resume.py`

## Installation
Simply clone this project and install required packages.

```sh
git clone https://github.com/weicc0202/ChuSI.git
cd ChuSI
pip3 install -r requirements.txt
```

## Before developing your chatbot
ChuSI is built on the LINE Message API, heroku, and AWS platform. To ensure that all the functions work well on your project, it is recommended to follow the guideline below and got the secret key and tokens for all of them. Key and tokens are required to access your resources.

1. https://developers.line.biz/en/docs/messaging-api/getting-started/
2. https://github.com/line/line-bot-sdk-java/tree/master/sample-spring-boot-echo#step-2
3. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html


## Heroku environment setup
To setup your Heroku deployment environment, use the heroku shell command for your setting. Replace **YOUR_LINE_CHANNEL_SECRET, YOUR_LINE_CHANNEL_ACCESS_TOKEN, YOUR_AWS_KEY_ID, YOUR_AWS_SECRET_ACCESS_KEY** with your true values.

**Notice: Don't uploade your keys to github for security issues!!!**

```sh
heroku create chusi
heroku git:remote -a chusi
heroku config:set LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
heroku config:set LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN
heroku config:set AWS_ACCESS_KEY_ID= YOUR_AWS_KEY_ID
heroku config:set AWS_SECRET_ACCESS_KEY= YOUR_AWS_SECRET_ACCESS_KEY
```

## Deployment
To deploy ChuSI to heroku, you might commit to git first, and deploy to heroku:
```sh
git add .
git commit -m "YOUR_DEDICATED_COMMIT_MESSAGE"
git push heroku main
```

If it cannot work well, dump out the logs to see what happened.
```sh
heroku logs
```

## Release History
* 0.2.0
    * CHANGE: Update docs `README.md`
    * CHANGE: Modify reply messages
    * CHAGNE: Modify interfaces in `agent.py` and `resume.py`
    * ADD: Add `update.py` module for tracking user's behavior with AWS DynamoDB
* 0.1.0
    * The first proper release
    * ADD: Add `suggest()` interface in `resume.py`
* 0.0.1
    * Work in progress

## Future Plan (Roadmap)
* NLU (Natural Language Understanding, Processing)
    * Currently use flow-based strategy to reply user messages.
    * Objective: Import intent-based and propose a hybrid solution for chatbot.

* Resume Segmentation and Understanding (Computer Vision)
    * Define a dedicated structure to represent resume
    * Currently rely on human knowledge to extract information by resume


## Meta

Weichu Chang – [@LinkedIn](https://www.linkedin.com/in/wei-chu-chang-9326b1129/) – ms0701515@gmail.com

<!-- Distributed under the XYZ license. See ``LICENSE`` for more information. -->

[https://github.com/weicc0202](https://github.com/weicc0202/)


<!-- ## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request -->

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki

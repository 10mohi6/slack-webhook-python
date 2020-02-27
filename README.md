# slack-webhook

[![PyPI](https://img.shields.io/pypi/v/slack-webhook)](https://pypi.org/project/slack-webhook/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/10mohi6/slack-webhook-python/branch/master/graph/badge.svg)](https://codecov.io/gh/10mohi6/slack-webhook-python)
[![Build Status](https://travis-ci.com/10mohi6/slack-webhook-python.svg?branch=master)](https://travis-ci.com/10mohi6/slack-webhook-python)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/slack-webhook)](https://pypi.org/project/slack-webhook/)
[![Downloads](https://pepy.tech/badge/slack-webhook)](https://pepy.tech/project/slack-webhook)

slack-webhook is a python client library for slack api Incoming Webhooks on Python 3.6 and above.


## Installation

    $ pip install slack-webhook

## Usage

### basic
```python
from slack_webhook import Slack

slack = Slack(url='https://hooks.slack.com/services/T00/B00/XXX')
slack.post(text="Hello, world.")
```

### advanced
```python
from slack_webhook import Slack

slack = Slack(url='https://hooks.slack.com/services/T00/B00/XXX')
slack.post(text="Robert DeSoto added a new task",
    attachments = [{
        "fallback": "Plan a vacation",
        "author_name": "Owner: rdesoto",
        "title": "Plan a vacation",
        "text": "I've been working too hard, it's time for a break.",
        "actions": [
            {
                "name": "action",
                "type": "button",
                "text": "Complete this task",
                "style": "",
                "value": "complete"
            },
            {
                "name": "tags_list",
                "type": "select",
                "text": "Add a tag...",
                "data_source": "static",
                "options": [
                    {
                        "text": "Launch Blocking",
                        "value": "launch-blocking"
                    },
                    {
                        "text": "Enhancement",
                        "value": "enhancement"
                    },
                    {
                        "text": "Bug",
                        "value": "bug"
                    }
                ]
            }
        ]
    }]
)
```

## Getting started

For help getting started with Incoming Webhooks, view our online [documentation](https://api.slack.com/incoming-webhooks).


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
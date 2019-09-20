import os, pytest
from slack_webhook import Slack

class TestSlack(object):

    def setup_method(self, method):
        url = os.environ['SLACK_WEBHOOK_URL']
        self.slack = Slack(url=url)

    def test_post_basic(self):

        expected = 'ok'
        actual = self.slack.post(text="Hello, world.")
        assert expected == actual

    def test_post_advanced(self):

        expected = 'ok'
        actual = self.slack.post(text = "Robert DeSoto added a new task", attachments=[
        {
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
        }])
        assert expected == actual

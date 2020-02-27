import os
import pytest
import time
from slack_webhook import Slack


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    url = os.environ["SLACK_WEBHOOK_URL"]
    yield Slack(url=url)


@pytest.fixture(scope="function", autouse=True)
def slack(scope_module):
    time.sleep(1)
    yield scope_module


# @pytest.mark.skip
def test_slack_post_basic(slack):
    expected = "ok"
    actual = slack.post(text="Hello, world.")
    assert expected == actual


# @pytest.mark.skip
def test_slack_post_advanced(slack):
    expected = "ok"
    actual = slack.post(
        text="Robert DeSoto added a new task",
        attachments=[
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
                        "value": "complete",
                    },
                    {
                        "name": "tags_list",
                        "type": "select",
                        "text": "Add a tag...",
                        "data_source": "static",
                        "options": [
                            {"text": "Launch Blocking", "value": "launch-blocking"},
                            {"text": "Enhancement", "value": "enhancement"},
                            {"text": "Bug", "value": "bug"},
                        ],
                    },
                ],
            }
        ],
    )
    assert expected == actual

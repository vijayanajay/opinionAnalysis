from behave import *
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'opinionanalysis.settings'
from getopinions import *


use_step_matcher("re")

@given("a feed")
def step_impl(context):
    context.feed = "http://www.livemint.com/rss/opinion"

@when("all the articles are extracted")
def step_impl(context):
    feed_content = getwebsite.get_feed(rssfeed)
    for entry in feed_content['entries']:
        article = Article()
        article.title = entry['title']
        article.content = entry['summary']
        article.link = entry['links'][0]['href']
        article.save()

@then(u'I see (?P<number>.*) feeds in the Article table')
def step_impl(context, number):
    """
    :type context behave.runner.Context
    """
    pass


@step("all the fields are filled in")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass
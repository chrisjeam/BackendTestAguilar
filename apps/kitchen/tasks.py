import requests, json, os
from celery import shared_task
from datetime import datetime
from apps.kitchen.models import Menu

def sendSlackMessage(id):
	today = datetime.now()
	menuQuery = Menu.objects.get(pk=id)
	# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
	url = "https://nora.cornershop.io/menu/{}".format(menuQuery.uuid)
	webhook_url = 'https://hooks.slack.com/services/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'
	slack_data = {
	"blocks": [
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "Hey... ya está listo el menú de hoy... Yumi!"
				}
			},
			{
				"type": "divider"
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": url
				}
			},
			{
				"type": "divider"
			}
		]
	}

	response = requests.post(
		webhook_url, data=json.dumps(slack_data),
		headers={'Content-Type': 'application/json'}
	)
	return response
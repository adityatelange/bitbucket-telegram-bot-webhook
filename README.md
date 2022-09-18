# Bitbucket WebHook Updates Telegram Bot

## introduction
```
This telegram bot uses webhooks to integrate applications with Bitbucket Cloud.

Without webhooks, if you want to detect when events occur in Bitbucket Cloud,
you need to poll the API. However, polling the API is inconvenient, inefficient, and error-prone.
Consider how SMS messages work on mobile phones.
You don't have to check your messages every 5 minutes to see if you have a text because your phone sends you a notification.
In the same way, webhooks work like the notification so that the API does not have to check for the same activity every minute.

more info : [Webhook Documentation](https://confluence.atlassian.com/bitbucket/manage-webhooks-735643732.html)
```

## setup =>
Bot must be hosted on server with having a domain name to work !

Webhooks do not work via polling method.
### Requirements
```
python3
pip
flask
telepot
```

### installation
```
$ git clone https://github.com/AdityaTelange/bitbucket-telegram-bot-webhook
$ cd bitbucket-telegram-bot-webhook
$ pip3 install --user -r requirements.txt
```

Edit *config.py* file
```
TOKEN='<bot_token_obtained_from_bot_father>'
OWNER_ID=<owner_id>
NOTIFY_GRP_IDS = [
    xxxxxxxxx,
    -yyyyyyyyy
]
```
sample
```
TOKEN='xxxxxxxxx:qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
OWNER_ID=123456789
NOTIFY_GRP_IDS = [
    123456789,
    -123456789,
    -987645321
]
```

### adding webhook to bibucket repo
1. Repository-settings => Webhooks (under Workflow) => Add Webhook

2. Fill in Details

    title: 'title'

    url: https://domain.com/bitbucket

3. choose _Triggers_ and other info.

4. *Save*

## Run

```
$ python3 server.py
```

## Done !!!

Add your bot to grps and fill grp_id's into config.py

Now any of the selected Triggers will send you a message !

### note:
1. [Telegram bot - how to get a group chat id?](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)
2. get owner id : send a message to [@userinfobot](https://telegram.me/userinfobot)
3. Group ids are ment to be added personally because it can cause security/privacy issues. Bot can be added/shared to any group under certain settings. Thus providing Notifs to Groups you may be not aware of!
4. Pull-request notifs aren't supported yet

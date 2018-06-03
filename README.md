# unable-concierge
Flask service that integrates facebook messenger with Conversations APP to create a life multilingual "chat room" between customer and hotel agent.

Documentation: https://hackpad.com/Unbabel-Concierge-hy7d9Uva6oO

This project requires a .env file:

#.env exemple:
DEBUG_MODE=False
PAGE_LANG=en
PAGE_EMAIL=*****@*****.com
WEBHOOK_ENDPOINT=https://89a12912.ngrok.io/conversation_update/
CONVERSATIONS_API=http://e3ae3e36.ngrok.io/
API_USERNAME=*******
API_KEY=85cdbb6968e9b96e62e6ad133a9a15
FACEBOOK_API=https://graph.facebook.com/v2.6/
FACEBOOK_PAGE_TOKEN=EAAMiRVs3I7sBAPYmX15BZApZCjoRRDjrjjKuZC1W9ZBdk6sGbSN6UiZBdWcLOkrZCPZBIsAN5vJvkJcBahw6cJ4BGIjZCsU0CCqIVg6wzgdfnVmxx9YoaGy84h7uKM4rKjDQK55SXWEwBZA6BxjDJIbunjiZBIPlH6gjynrTyZAqZAyCpwZDZD


API_USERNAME and API_KEY are the unbabel username and respective key.
PAGE_EMAIL is the email from the page were your notifications will apear everytime a customer starts a conversation.

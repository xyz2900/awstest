#!/usr/bin/env python
# tocaro webfookテスト
# curl -X POST --data-urlencode 'payload={"text": "This is test message. ex link http://example.com.", "attachments": [ { "title": "This is sample title", "value": "This is sample value" } ] }' https://hooks.tocaro.im/integrations/inbound_webhook/e76sq6cex2p5eng2m3miatqr3d69ysg3
# https://hooks.tocaro.im/integrations/inbound_webhook/e76sq6cex2p5eng2m3miatqr3d69ysg3
import requests
import json

if __name__ == '__main__':
   webhook_url = 'https://hooks.tocaro.im/integrations/inbound_webhook/c0fwo37klr5mith1zcawqufimigoqaph'

   payload = {
      "text": "This is sample message. link format is http://example.com",
      "color": "info",

      "attachments": [
         {
            "title": "This is sample title",
            "value": "This is sample value"
         },
         {
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c8/2016-03-03_13_43_30-チャート.png_-_Windows_Photo_Viewer.png"
         }
      ]
   }

   jdata = json.dumps(payload)

   content = {
      "payload": jdata
   }

   result = requests.post(webhook_url, content)
   print(result)




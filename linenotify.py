import requests

def lineNotifyMessage(token, msg):
      headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
	
      payload = {'message': msg}
      r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
      return r.status_code
	
message = 'Notify from LINE, HELLO WORLD'
token = 'VVQ1VIxvOss8jgUx9hneghKQmRJZt70aMHQ88vVR8eH'

lineNotifyMessage(token, message)
"""
looking at using - https://www.polar.com/accesslink-api/?shell#making-requests
"""

import requests



f"https://flow.polar.com/oauth2/authorization?response_type=code&client_id={POLAR_CLIENT_ID}"

headers = {
  'Content-Type': 'application/xml',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://www.polaraccesslink.com/v3/users', params={

}, headers = headers)

print r.json()








import requests
headers = {
  'Accept': '*/*',
  'Authorization': 'Bearer {access-token}'
}



r = requests.get('https://www.polaraccesslink.com/v3/users/{user-id}/exercise-transactions/{transaction-id}/exercises/{exercise-id}/fit', params={

}, headers = headers)

print r.json()


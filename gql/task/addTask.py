import requests
import json

url = "https://valvir-opus.tracelink.com/api/graphql"

payload = "{\"query\":\"mutation AddTask($action: String!, $payload: JSON!)\\n{\\n    genericActionCall(action: $action, payload: $payload)\\n    {\\n    result\\n    __typename\\n    }    \\n}\",\"variables\":{\"action\":\"Addtask\",\"payload\":{\"templateId\":\"9f2ce4b7-b9fe-4273-9586-c58c78f76b85\",\"aptBusinessObjectSummary\":\"GraphQL Python created task\",\"aptBusinessObjectDescription\":\"Tasks for recurring purchase orders\",\"businessPriority\":\"LOW\",\"completionDueDate\":\"1737834411000\",\"isVisible\":true,\"isAtRisk\":false}}}"
headers = {
  'Authorization': 'Basic YOUR_TOKEN',
  'Content-Type': 'application/json',
  'Dataspace': 'default',
  'companyId': 'YOUR_COMPANY_ID',
  'processNetworkId': 'YOUR_PROCESS_NETWORK_ID'
  }

response = requests.request("POST", url, headers=headers, data=payload)

raw_json = json.loads(response.text)  # load the text result to into json

schema_json = raw_json.get('data').get('genericActionCall')  # drill into object
# schema_json = raw_json.get('data').get('genericGetObject') # use this for getObjectCalls
api_json = json.loads(schema_json.get('result'))  # load the result object to json

# for genericGetObject, use schema_json. for genericActionCall, use api_json.
print(json.dumps(api_json, indent=4, sort_keys=False))  # 'pretty print' the result

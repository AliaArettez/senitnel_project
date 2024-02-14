import json

import Api_resources as API
# enter elements (workspace ID, shared key)  Could be found in workspace_settings -> agents
# Update the customer ID to your Log Analytics workspace ID
#customer_id = 'xxxx-xxxx-xxxx-xxxx-xxxx'
print("Enter id of sentinel workspace:")
customer_id = input()

# For the shared key, use either the primary or the secondary Connected Sources client authentication key
#shared_key = "xxxxx"

print("Enter authentication key for workspace:")
shared_key = input()
# The log type is the name of the event that is being submitted
# aka. table name, although the full name would be "Test_CL" in Sentinel.
#log_type = 'Test'
print("Enter name for table it's suppose to be inserted:")
log_type = input()


# An example JSON web monitor object through file. Go to data.json for changing input.
# beware that elements are supposed to have the same names of values or the new column will be made in sentinel
print("enter name (path) of json file without .json at the end ")
file_name = input()
f = open(file_name + ".json")

#f= open(data.json)
json_data = json.load(f)
body = json.dumps(json_data)
API.post_data(customer_id, shared_key, body, log_type)
# GetServiceBrokerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**relationships** | [**Dict[str, ToOneRelationship]**](ToOneRelationship.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_service_broker_response import GetServiceBrokerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceBrokerResponse from a JSON string
get_service_broker_response_instance = GetServiceBrokerResponse.from_json(json)
# print the JSON string representation of the object
print(GetServiceBrokerResponse.to_json())

# convert the object into a dict
get_service_broker_response_dict = get_service_broker_response_instance.to_dict()
# create an instance of GetServiceBrokerResponse from a dict
get_service_broker_response_from_dict = GetServiceBrokerResponse.from_dict(get_service_broker_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



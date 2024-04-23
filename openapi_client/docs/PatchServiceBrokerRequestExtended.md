# PatchServiceBrokerRequestExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**authentication** | [**Authentication**](Authentication.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**authentication_current** | [**Authentication**](Authentication.md) |  | [optional] 

## Example

```python
from openapi_client.models.patch_service_broker_request_extended import PatchServiceBrokerRequestExtended

# TODO update the JSON string below
json = "{}"
# create an instance of PatchServiceBrokerRequestExtended from a JSON string
patch_service_broker_request_extended_instance = PatchServiceBrokerRequestExtended.from_json(json)
# print the JSON string representation of the object
print(PatchServiceBrokerRequestExtended.to_json())

# convert the object into a dict
patch_service_broker_request_extended_dict = patch_service_broker_request_extended_instance.to_dict()
# create an instance of PatchServiceBrokerRequestExtended from a dict
patch_service_broker_request_extended_from_dict = PatchServiceBrokerRequestExtended.from_dict(patch_service_broker_request_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



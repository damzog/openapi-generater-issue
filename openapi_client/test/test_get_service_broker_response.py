# coding: utf-8

"""
    Cloudfoundry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_service_broker_response import GetServiceBrokerResponse

class TestGetServiceBrokerResponse(unittest.TestCase):
    """GetServiceBrokerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetServiceBrokerResponse:
        """Test GetServiceBrokerResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetServiceBrokerResponse`
        """
        model = GetServiceBrokerResponse()
        if include_optional:
            return GetServiceBrokerResponse(
                guid = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                url = '',
                relationships = {
                    'key' : openapi_client.models.to_one_relationship.ToOneRelationship(
                        data = {
                            'key' : ''
                            }, )
                    },
                metadata = openapi_client.models.metadata.Metadata(
                    labels = {
                        'key' : ''
                        }, 
                    annotations = {
                        'key' : ''
                        }, ),
                links = {
                    'key' : openapi_client.models.link.Link(
                        href = '', )
                    }
            )
        else:
            return GetServiceBrokerResponse(
                guid = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                url = '',
        )
        """

    def testGetServiceBrokerResponse(self):
        """Test GetServiceBrokerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

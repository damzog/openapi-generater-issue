# coding: utf-8

"""
    Cloudfoundry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.link import Link

class TestLink(unittest.TestCase):
    """Link unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Link:
        """Test Link
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Link`
        """
        model = Link()
        if include_optional:
            return Link(
                href = ''
            )
        else:
            return Link(
                href = '',
        )
        """

    def testLink(self):
        """Test Link"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

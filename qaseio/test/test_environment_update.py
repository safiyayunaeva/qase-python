# coding: utf-8

"""
    Qase.io TestOps API

    Qase TestOps API Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from qaseio.models.environment_update import EnvironmentUpdate

class TestEnvironmentUpdate(unittest.TestCase):
    """EnvironmentUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentUpdate:
        """Test EnvironmentUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnvironmentUpdate`
        """
        model = EnvironmentUpdate()
        if include_optional:
            return EnvironmentUpdate(
                title = '',
                description = '',
                slug = '',
                host = ''
            )
        else:
            return EnvironmentUpdate(
        )
        """

    def testEnvironmentUpdate(self):
        """Test EnvironmentUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

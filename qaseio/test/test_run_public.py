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

from qaseio.models.run_public import RunPublic

class TestRunPublic(unittest.TestCase):
    """RunPublic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RunPublic:
        """Test RunPublic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunPublic`
        """
        model = RunPublic()
        if include_optional:
            return RunPublic(
                status = True
            )
        else:
            return RunPublic(
                status = True,
        )
        """

    def testRunPublic(self):
        """Test RunPublic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

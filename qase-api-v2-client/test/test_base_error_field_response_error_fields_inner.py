# coding: utf-8

"""
    Qase.io TestOps API v2

    Qase TestOps API v2 Specification.

    The version of the OpenAPI document: 2.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qase.api_client_v2.models.base_error_field_response_error_fields_inner import BaseErrorFieldResponseErrorFieldsInner

class TestBaseErrorFieldResponseErrorFieldsInner(unittest.TestCase):
    """BaseErrorFieldResponseErrorFieldsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseErrorFieldResponseErrorFieldsInner:
        """Test BaseErrorFieldResponseErrorFieldsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseErrorFieldResponseErrorFieldsInner`
        """
        model = BaseErrorFieldResponseErrorFieldsInner()
        if include_optional:
            return BaseErrorFieldResponseErrorFieldsInner(
                field = '',
                error = ''
            )
        else:
            return BaseErrorFieldResponseErrorFieldsInner(
        )
        """

    def testBaseErrorFieldResponseErrorFieldsInner(self):
        """Test BaseErrorFieldResponseErrorFieldsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
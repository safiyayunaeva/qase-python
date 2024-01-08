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

from qaseio.models.suite_list_response import SuiteListResponse

class TestSuiteListResponse(unittest.TestCase):
    """SuiteListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SuiteListResponse:
        """Test SuiteListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SuiteListResponse`
        """
        model = SuiteListResponse()
        if include_optional:
            return SuiteListResponse(
                status = True,
                result = qaseio.models.suite_list_response_all_of_result.SuiteListResponse_allOf_result(
                    total = 56, 
                    filtered = 56, 
                    count = 56, 
                    entities = [
                        qaseio.models.suite.Suite(
                            id = 56, 
                            title = '', 
                            description = '', 
                            preconditions = '', 
                            position = 56, 
                            cases_count = 56, 
                            parent_id = 56, 
                            created = '2021-12-30 19:23:59', 
                            updated = '2021-12-30 19:23:59', 
                            created_at = '2021-12-30T19:23:59Z', 
                            updated_at = '2021-12-30T19:23:59Z', )
                        ], )
            )
        else:
            return SuiteListResponse(
        )
        """

    def testSuiteListResponse(self):
        """Test SuiteListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

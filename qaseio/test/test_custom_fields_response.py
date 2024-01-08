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

from qaseio.models.custom_fields_response import CustomFieldsResponse

class TestCustomFieldsResponse(unittest.TestCase):
    """CustomFieldsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomFieldsResponse:
        """Test CustomFieldsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomFieldsResponse`
        """
        model = CustomFieldsResponse()
        if include_optional:
            return CustomFieldsResponse(
                status = True,
                result = qaseio.models.custom_fields_response_all_of_result.CustomFieldsResponse_allOf_result(
                    total = 56, 
                    filtered = 56, 
                    count = 56, 
                    entities = [
                        qaseio.models.custom_field.CustomField(
                            id = 56, 
                            title = '', 
                            entity = '', 
                            type = '', 
                            placeholder = '', 
                            default_value = '', 
                            value = '', 
                            is_required = True, 
                            is_visible = True, 
                            is_filterable = True, 
                            is_enabled_for_all_projects = True, 
                            created = '2021-12-30 19:23:59', 
                            updated = '2021-12-30 19:23:59', 
                            created_at = '2021-12-30T19:23:59Z', 
                            updated_at = '2021-12-30T19:23:59Z', 
                            projects_codes = [
                                ''
                                ], )
                        ], )
            )
        else:
            return CustomFieldsResponse(
        )
        """

    def testCustomFieldsResponse(self):
        """Test CustomFieldsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

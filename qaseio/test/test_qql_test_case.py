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

from qaseio.models.qql_test_case import QqlTestCase

class TestQqlTestCase(unittest.TestCase):
    """QqlTestCase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QqlTestCase:
        """Test QqlTestCase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QqlTestCase`
        """
        model = QqlTestCase()
        if include_optional:
            return QqlTestCase(
                id = 56,
                position = 56,
                title = '',
                description = '',
                preconditions = '',
                postconditions = '',
                severity = 56,
                priority = 56,
                type = 56,
                layer = 56,
                is_flaky = 56,
                behavior = 56,
                automation = 56,
                status = 56,
                milestone_id = 56,
                suite_id = 56,
                custom_fields = [
                    qaseio.models.custom_field_value.CustomFieldValue(
                        id = 56, 
                        value = '', )
                    ],
                attachments = [
                    qaseio.models.attachment.Attachment(
                        size = 56, 
                        mime = '', 
                        filename = '', 
                        url = '', )
                    ],
                steps_type = '',
                steps = [
                    qaseio.models.test_step.TestStep(
                        hash = '', 
                        shared_step_hash = '', 
                        shared_step_nested_hash = '', 
                        position = 56, 
                        action = '', 
                        expected_result = '', 
                        data = '', 
                        attachments = [
                            qaseio.models.attachment.Attachment(
                                size = 56, 
                                mime = '', 
                                filename = '', 
                                url = '', )
                            ], 
                        steps = [
                            None
                            ], )
                    ],
                params = None,
                tags = [
                    qaseio.models.tag_value.TagValue(
                        title = '', 
                        internal_id = 56, )
                    ],
                member_id = 56,
                author_id = 56,
                created_at = '2021-12-30T19:23:59Z',
                updated_at = '2021-12-30T19:23:59Z'
            )
        else:
            return QqlTestCase(
        )
        """

    def testQqlTestCase(self):
        """Test QqlTestCase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

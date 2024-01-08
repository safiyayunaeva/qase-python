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

from qaseio.models.test_case_list_response_all_of_result import TestCaseListResponseAllOfResult

class TestTestCaseListResponseAllOfResult(unittest.TestCase):
    """TestCaseListResponseAllOfResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestCaseListResponseAllOfResult:
        """Test TestCaseListResponseAllOfResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestCaseListResponseAllOfResult`
        """
        model = TestCaseListResponseAllOfResult()
        if include_optional:
            return TestCaseListResponseAllOfResult(
                total = 56,
                filtered = 56,
                count = 56,
                entities = [
                    qaseio.models.test_case.TestCase(
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
                                data = '', )
                            ], 
                        params = null, 
                        tags = [
                            qaseio.models.tag_value.TagValue(
                                title = '', 
                                internal_id = 56, )
                            ], 
                        member_id = 56, 
                        author_id = 56, 
                        created_at = '2021-12-30T19:23:59Z', 
                        updated_at = '2021-12-30T19:23:59Z', 
                        deleted = '2021-12-30T19:23:59.000000Z', 
                        created = '2021-12-30T19:23:59.000000Z', 
                        updated = '2021-12-30T19:23:59.000000Z', 
                        external_issues = [
                            qaseio.models.external_issue.ExternalIssue(
                                type = '', 
                                issues = [
                                    qaseio.models.external_issue_issues_inner.ExternalIssue_issues_inner(
                                        id = '', 
                                        link = '', )
                                    ], )
                            ], )
                    ]
            )
        else:
            return TestCaseListResponseAllOfResult(
        )
        """

    def testTestCaseListResponseAllOfResult(self):
        """Test TestCaseListResponseAllOfResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

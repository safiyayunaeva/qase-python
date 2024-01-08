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

from qaseio.models.create_results_request_v2 import CreateResultsRequestV2

class TestCreateResultsRequestV2(unittest.TestCase):
    """CreateResultsRequestV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateResultsRequestV2:
        """Test CreateResultsRequestV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateResultsRequestV2`
        """
        model = CreateResultsRequestV2()
        if include_optional:
            return CreateResultsRequestV2(
                results = [
                    qaseio.models.result_create_v2.ResultCreateV2(
                        id = '', 
                        title = '', 
                        signature = '', 
                        testops_id = 56, 
                        execution = qaseio.models.result_execution.ResultExecution(
                            start_time = 1.337, 
                            end_time = 1.337, 
                            status = '', 
                            duration = 56, 
                            stacktrace = '', 
                            thread = '', ), 
                        fields = {
                            'key' : ''
                            }, 
                        attachments = [
                            qaseio.models.result_attachment.ResultAttachment(
                                id = '', 
                                file_name = '', 
                                mime_type = '', 
                                file_path = '', 
                                content = '', 
                                size = 56, )
                            ], 
                        steps = [
                            qaseio.models.result_step.ResultStep(
                                id = '', 
                                step_type = '', 
                                data = qaseio.models.result_step_data.ResultStepData(
                                    action = '', 
                                    expected_result = '', ), 
                                parent_id = '', )
                            ], 
                        params = {
                            'key' : ''
                            }, 
                        author = '', 
                        relations = qaseio.models.relation.Relation(
                            suite = qaseio.models.relation_suite.RelationSuite(
                                data = [
                                    qaseio.models.relation_suite_item.RelationSuiteItem(
                                        title = '', 
                                        public_id = 56, )
                                    ], ), ), 
                        muted = True, 
                        message = '', 
                        created_at = 1.337, )
                    ]
            )
        else:
            return CreateResultsRequestV2(
        )
        """

    def testCreateResultsRequestV2(self):
        """Test CreateResultsRequestV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Qase.io TestOps API v1

    Qase TestOps API v1 Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qase.api_client_v1.models.result_list_response import ResultListResponse

class TestResultListResponse(unittest.TestCase):
    """ResultListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResultListResponse:
        """Test ResultListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResultListResponse`
        """
        model = ResultListResponse()
        if include_optional:
            return ResultListResponse(
                status = True,
                result = qase.api_client_v1.models.result_list_response_all_of_result.ResultListResponse_allOf_result(
                    total = 56, 
                    filtered = 56, 
                    count = 56, 
                    entities = [
                        qase.api_client_v1.models.result.Result(
                            hash = '', 
                            comment = '', 
                            stacktrace = '', 
                            run_id = 56, 
                            case_id = 56, 
                            steps = [
                                qase.api_client_v1.models.test_step_result.TestStepResult(
                                    status = 56, 
                                    position = 56, 
                                    attachments = [
                                        qase.api_client_v1.models.attachment.Attachment(
                                            size = 56, 
                                            mime = '', 
                                            filename = '', 
                                            url = '', )
                                        ], )
                                ], 
                            status = '', 
                            is_api_result = True, 
                            time_spent_ms = 56, 
                            end_time = '2021-12-30T19:23:59Z', 
                            attachments = [
                                qase.api_client_v1.models.attachment.Attachment(
                                    size = 56, 
                                    mime = '', 
                                    filename = '', 
                                    url = '', )
                                ], )
                        ], )
            )
        else:
            return ResultListResponse(
        )
        """

    def testResultListResponse(self):
        """Test ResultListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

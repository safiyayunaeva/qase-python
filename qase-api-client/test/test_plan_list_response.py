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

from qase.api_client_v1.models.plan_list_response import PlanListResponse

class TestPlanListResponse(unittest.TestCase):
    """PlanListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanListResponse:
        """Test PlanListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanListResponse`
        """
        model = PlanListResponse()
        if include_optional:
            return PlanListResponse(
                status = True,
                result = qase.api_client_v1.models.plan_list_response_all_of_result.PlanListResponse_allOf_result(
                    total = 56, 
                    filtered = 56, 
                    count = 56, 
                    entities = [
                        qase.api_client_v1.models.plan.Plan(
                            id = 56, 
                            title = '', 
                            description = '', 
                            cases_count = 56, 
                            created_at = '2021-12-30T19:23:59Z', 
                            updated_at = '2021-12-30T19:23:59Z', 
                            created = '2021-12-30 19:23:59', 
                            updated = '2021-12-30 19:23:59', )
                        ], )
            )
        else:
            return PlanListResponse(
        )
        """

    def testPlanListResponse(self):
        """Test PlanListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

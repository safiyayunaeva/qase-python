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

from qaseio.models.project_counts import ProjectCounts

class TestProjectCounts(unittest.TestCase):
    """ProjectCounts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectCounts:
        """Test ProjectCounts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectCounts`
        """
        model = ProjectCounts()
        if include_optional:
            return ProjectCounts(
                cases = 56,
                suites = 56,
                milestones = 56,
                runs = qaseio.models.project_counts_runs.Project_counts_runs(
                    total = 56, 
                    active = 56, ),
                defects = qaseio.models.project_counts_defects.Project_counts_defects(
                    total = 56, 
                    open = 56, )
            )
        else:
            return ProjectCounts(
        )
        """

    def testProjectCounts(self):
        """Test ProjectCounts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

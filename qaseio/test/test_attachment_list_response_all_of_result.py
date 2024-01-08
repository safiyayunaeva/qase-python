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

from qaseio.models.attachment_list_response_all_of_result import AttachmentListResponseAllOfResult

class TestAttachmentListResponseAllOfResult(unittest.TestCase):
    """AttachmentListResponseAllOfResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachmentListResponseAllOfResult:
        """Test AttachmentListResponseAllOfResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachmentListResponseAllOfResult`
        """
        model = AttachmentListResponseAllOfResult()
        if include_optional:
            return AttachmentListResponseAllOfResult(
                total = 56,
                filtered = 56,
                count = 56,
                entities = [
                    qaseio.models.attachment_get.AttachmentGet(
                        hash = '', 
                        file = '', 
                        mime = '', 
                        size = 56, 
                        extension = '', 
                        full_path = '', )
                    ]
            )
        else:
            return AttachmentListResponseAllOfResult(
        )
        """

    def testAttachmentListResponseAllOfResult(self):
        """Test AttachmentListResponseAllOfResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

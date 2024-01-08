# coding: utf-8

"""
    Qase.io TestOps API

    Qase TestOps API Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ResultStepExecution(BaseModel):
    """
    ResultStepExecution
    """ # noqa: E501
    start_time: Optional[Union[StrictFloat, StrictInt]] = None
    end_time: Optional[Union[StrictFloat, StrictInt]] = None
    status: Optional[StrictStr] = None
    duration: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["start_time", "end_time", "status", "duration"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ResultStepExecution from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if start_time (nullable) is None
        # and model_fields_set contains the field
        if self.start_time is None and "start_time" in self.model_fields_set:
            _dict['start_time'] = None

        # set to None if end_time (nullable) is None
        # and model_fields_set contains the field
        if self.end_time is None and "end_time" in self.model_fields_set:
            _dict['end_time'] = None

        # set to None if duration (nullable) is None
        # and model_fields_set contains the field
        if self.duration is None and "duration" in self.model_fields_set:
            _dict['duration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ResultStepExecution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "start_time": obj.get("start_time"),
            "end_time": obj.get("end_time"),
            "status": obj.get("status"),
            "duration": obj.get("duration")
        })
        return _obj



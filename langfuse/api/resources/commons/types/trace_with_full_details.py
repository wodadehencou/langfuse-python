# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import pydantic_v1
from .observations_view import ObservationsView
from .score import Score
from .trace import Trace


class TraceWithFullDetails(Trace):
    html_path: str = pydantic_v1.Field(alias="htmlPath")
    """
    Path of trace in Langfuse UI
    """

    total_cost: float = pydantic_v1.Field(alias="totalCost")
    """
    Cost of trace in USD
    """

    observations: typing.List[ObservationsView]
    scores: typing.List[Score]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}

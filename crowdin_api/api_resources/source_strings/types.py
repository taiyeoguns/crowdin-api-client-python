from typing import Any, Union, Mapping

from crowdin_api.api_resources.enums import BatchPatchOperation, PatchOperation
from crowdin_api.api_resources.source_strings.enums import SourceStringsPatchPath
from crowdin_api.typing import TypedDict


class SourceStringsPatchRequest(TypedDict):
    value: Any
    op: PatchOperation
    path: SourceStringsPatchPath


class SourceStringsBatchPatchRequest(TypedDict):
    value: Union[str, Mapping, int, bool]
    op: BatchPatchOperation
    path: str

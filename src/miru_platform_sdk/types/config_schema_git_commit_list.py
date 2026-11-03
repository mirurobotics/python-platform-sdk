# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .shared.paginated_list import PaginatedList
from .config_schema_git_commit import ConfigSchemaGitCommit

__all__ = ["ConfigSchemaGitCommitList"]


class ConfigSchemaGitCommitList(PaginatedList):
    data: List[ConfigSchemaGitCommit]
    """The list of config schema git commits."""

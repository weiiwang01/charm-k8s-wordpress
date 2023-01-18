# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Module for commonly used internal types in wordpress charm."""

from typing import Any, NamedTuple, Union


class CommandExecResult(NamedTuple):
    """Result of executed command from wordpress container.

    Attrs:
        return_code: exit code from executed command.
        stdout: standard output from the executed command.
        stderr: standard error output from the executed command.
    """

    return_code: int
    stdout: Union[str, bytes]
    stderr: Union[str, bytes, None]


class ExecResult(NamedTuple):
    """Wrapper for executed command result from wordpress container.

    Attrs:
        success: True if command successful, else False.
        result: returned value from execution command, parsed in desired format.
        message: Error message output of executed command.
    """

    success: bool
    result: Any
    message: str

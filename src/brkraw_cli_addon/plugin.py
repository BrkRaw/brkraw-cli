"""brkraw.cli entry point implementation."""

from __future__ import annotations

import argparse


def _run(args: argparse.Namespace) -> int:
    print(args.message)
    return 0


def register(subparsers: argparse._SubParsersAction) -> None:  # type: ignore[name-defined]
    parser = subparsers.add_parser(
        "foo",
        help="Example foo command",
        description="Example foo command registered via brkraw.cli",
    )
    parser.add_argument(
        "message",
        nargs="?",
        default="Hello from brkraw addon",
        help="Message to print",
    )
    parser.set_defaults(_handler=_run)

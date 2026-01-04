# brkraw CLI extension template

Use this repository as a GitHub template to add a new command to `brkraw` via
the `brkraw.cli` entry point group. Extensions own their feature dependencies,
keeping the core `brkraw` install minimal and the maintenance surface small.

## Quick start

```bash
pip install -e .
brkraw foo --help
```

## Customize

Update these locations to match your extension:

- `pyproject.toml`: update `name`, `version`, and the entry point key under
  `[project.entry-points."brkraw.cli"]`.
- `src/brkraw_cli_addon/`: rename this package folder and update references
  (e.g., `src/my_addon/` and `my_addon.plugin:register`).
- `src/brkraw_cli_addon/plugin.py`: rename the command from `foo` (or any
  placeholder) and adjust help/description text.
- `src/brkraw_cli_addon/__init__.py`: keep the version in sync.

Example entry point after renaming:

```toml
[project.entry-points."brkraw.cli"]
mycmd = "my_addon.plugin:register"
```

## How it works

`brkraw` loads entry points in the `brkraw.cli` group. Each entry point must
resolve to a callable with this signature:

```python
def register(subparsers: argparse._SubParsersAction) -> None:
    ...
```

Inside `register`, define your subcommand and attach a handler:

```python
parser.set_defaults(_handler=handler_func)
```

## Layout

- `pyproject.toml`: packaging metadata and entry point configuration
- `src/brkraw_cli_addon/plugin.py`: CLI registration and command logic
- `src/brkraw_cli_addon/__init__.py`: version marker

## Development

```bash
pip install -e .
brkraw foo "hello from my extension"
```

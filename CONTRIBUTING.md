# Contributing

Thanks for helping improve OneDragon.

## Development Guidelines

- Keep changes focused and easy to review.
- Prefer configuration over hard-coded local paths.
- Keep generated scan results out of git.
- Document behavior changes in `README.md` or `CHANGELOG.md`.
- Use clear commit messages, for example `docs: clarify setup steps` or `fix: validate target file argument`.

## Before Opening a Pull Request

Run a quick syntax check:

```bash
python3 -m compileall start.py module
```

If your change touches scan behavior, include a short note describing:

- The authorized test environment used.
- The expected output files.
- Any external tools required to reproduce the result.

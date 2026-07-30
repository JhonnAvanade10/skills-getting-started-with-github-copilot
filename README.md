# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey JhonnAvanade10!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/JhonnAvanade10/skills-getting-started-with-github-copilot/issues/1)

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

**Development**

- **Run tests:** Activate the project virtualenv and run the test suite with pytest from the repository root.

```bash
. .venv/bin/activate
pytest -q
```

- **Do not run test modules directly with `python tests/...`:** executing a test file with plain python does not add the project root to `sys.path`, so imports like `import src.app` will raise `ModuleNotFoundError`. `pytest` configures the import path correctly.

- **If you need to run a test file directly** (not recommended), set `PYTHONPATH` first:

```bash
PYTHONPATH=. .venv/bin/python tests/test_app.py
```

- **Helper file:** We include [tests/conftest.py](tests/conftest.py#L1-L12) which ensures the project root is available when tests are executed via `pytest`.

- **Editor (Pylance) tips:** If your editor reports missing imports for test-time-only packages, select the interpreter at `.venv/bin/python` (Command Palette → Python: Select Interpreter) or add a workspace setting that adds the `src` folder to analysis paths.


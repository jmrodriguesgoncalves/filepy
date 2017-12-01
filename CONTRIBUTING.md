# Contributing

## Pull Requests

If you want to contribute to the repository, here's a quick guide:

1. Fork the repository
1. Develop and test your code changes with [pytest].
    * Respect the original code [style guide][styleguide].
    * Only use spaces for indentation.
    * Create minimal diffs - disable on save actions like reformat source code or organize imports. If you feel the source code should be reformatted create a separate PR for this change.
    * Check for unnecessary whitespace with `git diff --check` before committing.
    * Make sure your code supports Python 2.7, 3.4, 3.5 and 3.6. You can use `pyenv` and `tox` for this
1. Make the test pass
1. Commit your changes
1. Push to your fork and submit a pull request

## Running the tests

Make sure you have the latest version of Python downloaded on your computer.

1. Clone this repository:
    ```sh
    git clone https://github.com/jmrodriguesgoncalves/filepy
    ```
1. Install the sdk as an editable package using the current source:
    ```sh
    pip install --editable .
    ```
1. Install the test dependencies with:
    ```sh
    pip install pytest
    ```
    ```sh
    pytest test_build.py
    ```

## Additional Resources

* [General GitHub documentation](https://help.github.com/)
* [GitHub pull request documentation](https://help.github.com/send-pull-requests/)
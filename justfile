# justfile

# List available commands
default:
    just --list

# Install dependencies in a poetry-managed virtualenv
install:
    poetry install

# Run tests with pytest
test:
    poetry run pytest tests/

# Run linter checks (flake8, mypy, black)
lint:
    poetry run flake8 src tests
    poetry run mypy src tests
    poetry run black --check src tests

# Format code with black and isort
format:
    poetry run black src tests
    poetry run isort src tests

# Build the package
build:
    poetry build

# Publish to real PyPI (ensure pypi-token.pypi is set)
publish:
    poetry publish

# Clean build artifacts, caches, and temporary files
clean:
    # Clean Python and build artifacts
    find . -type d -name "__pycache__" -o -name "*.egg-info" -o -name ".ipynb_checkpoints" | xargs rm -rf
    find . -type f -name "*.py[co]" -delete
    rm -rf dist/ build/ .mypy_cache/ .pytest_cache/ .coverage htmlcov/
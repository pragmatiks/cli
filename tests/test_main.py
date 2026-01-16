"""Tests for CLI main entry point."""

import pytest
from typer.testing import CliRunner

from pragma_cli.main import app


@pytest.fixture
def cli_runner():
    return CliRunner()


def test_version_flag(cli_runner):
    """Test --version flag displays version and exits."""
    result = cli_runner.invoke(app, ["--version"])

    assert result.exit_code == 0
    # Should output "pragma X.Y.Z" format
    assert result.stdout.startswith("pragma ")
    # Version should have at least major.minor format
    version_parts = result.stdout.strip().split(" ")[1].split(".")
    assert len(version_parts) >= 2


def test_version_flag_short(cli_runner):
    """Test -V short flag also displays version."""
    result = cli_runner.invoke(app, ["-V"])

    assert result.exit_code == 0
    assert result.stdout.startswith("pragma ")


def test_help_shows_version_option(cli_runner):
    """Test that --help includes --version option."""
    result = cli_runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "--version" in result.stdout
    assert "-V" in result.stdout

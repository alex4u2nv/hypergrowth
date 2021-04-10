from example.entrypoint import cli
from click.testing import CliRunner


def test_full_execution():
    runner = CliRunner()
    name = "testing"
    result = runner.invoke(cli, ['one', 'do-stuff', name])
    assert result.exit_code == 0
    assert f"doing it {name} 1" in result.stdout
    assert "local-client" in result.stdout
    assert "context" in result.stdout

from src.scamguard.cli import main


def test_cli_output(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "scamguard",
            "Urgent! Send your OTP immediately.",
        ],
    )

    main()

    output = capsys.readouterr().out

    assert "ScamGuard" in output
    assert "Risk:" in output
    assert "Score:" in output
    assert "Credential" in output

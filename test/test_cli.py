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

def test_cli_missing_file(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "scamguard",
            "--file",
            "missing-message.txt",
        ],
    )

    try:
        main()
    except SystemExit:
        pass

    captured = capsys.readouterr()

    assert "File not found" in captured.err


def test_cli_empty_message(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "scamguard",
            "",
        ],
    )

    try:
        main()
    except SystemExit:
        pass

    captured = capsys.readouterr()

    assert "Message cannot be empty" in captured.err

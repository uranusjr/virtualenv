from __future__ import absolute_import, unicode_literals

import sys

import pytest

from virtualenv.activation import PowerShellActivator
from virtualenv.info import PY2

if PY2:
    from pipes import quote
else:
    from shlex import quote


@pytest.mark.slow
def test_powershell(activation_tester_class, activation_tester, monkeypatch):
    monkeypatch.setenv("TERM", "xterm")

    class PowerShell(activation_tester_class):
        def __init__(self, session):
            cmd = "powershell.exe" if sys.platform == "win32" else "pwsh"
            super(PowerShell, self).__init__(PowerShellActivator, session, cmd, "activate.ps1", "ps1")
            self._version_cmd = [cmd, "-c", "$PSVersionTable"]
            self._invoke_script = [cmd, "-ExecutionPolicy", "ByPass", "-File"]
            self.activate_cmd = "."
            self.script_encoding = "utf-16"

        def quote(self, s):
            """powershell double double quote needed for quotes within single quotes"""
            return quote(s).replace('"', '""')

        def _get_test_lines(self, activate_script):
            # for BATCH utf-8 support need change the character code page to 650001
            return super(PowerShell, self)._get_test_lines(activate_script)

        def invoke_script(self):
            return [self.cmd, "-File"]

        def print_prompt(self):
            return "prompt"

    activation_tester(PowerShell)

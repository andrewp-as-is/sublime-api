#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import StringIO
import sys
import sublime
import sublime_plugin


class SublimeApiCommand(sublime_plugin.WindowCommand):

    def run(self):
        try:
            path = self.window.active_view().file_name()
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            code = compile(open(path).read(), path, 'exec')
            try:
                exec(code, {}, {})
                out = sys.stdout.getvalue()
            except Exception as e:
                out = str(e)
            sys.stdout = old_stdout

            # output
            self.output_view = self.window.get_output_panel("textarea")
            self.window.run_command("show_panel", {"panel": "output.textarea"})
            self.output_view.set_read_only(False)
            self.output_view.run_command("append", {"characters": out})
            self.output_view.set_read_only(True)
        except Exception as e:
            sublime.error_message(str(e))

"""
example_plugin.py
Minimal Hunt Proxy plugin example.

Contract: expose either
    def create_widget(main_window) -> QWidget
or
    class PluginTab(QWidget): __init__(self, main_window)

`main_window` is the live HuntGUI instance, so you can reach things like
main_window.findings, main_window.requester_tab, main_window._project_paths.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit


def create_widget(main_window):
    return _NoteCounterWidget(main_window)


class _NoteCounterWidget(QWidget):
    """Tiny demo: counts findings currently loaded and shows a scratchpad."""

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout(self)

        self.info_label = QLabel()
        layout.addWidget(self.info_label)

        refresh_btn = QPushButton("Refresh finding count")
        refresh_btn.clicked.connect(self._refresh)
        layout.addWidget(refresh_btn)

        self.notes = QTextEdit()
        self.notes.setPlaceholderText("Scratch notes (not saved anywhere yet)...")
        layout.addWidget(self.notes)

        self._refresh()

    def _refresh(self):
        count = len(getattr(self.main_window, "findings", []))
        self.info_label.setText(f"Findings currently loaded: {count}")

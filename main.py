#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : zenk
# 2017-02-05 14:25

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def main():
    app = QApplication([""])

    # Build the window widget
    w = QWidget()
    w.setGeometry(300, 300, 250, 150)  # x, y, w, h
    w.setWindowTitle("My First Qt App")

    # Add a label with tooltip
    label = QLabel("Hello World  🚀", w)
    label.setToolTip("This is a <b>QLabel</b> widget with Tooltip")
    label.resize(label.sizeHint())
    label.move(80, 50)

    # Show window and run
    w.show()
    app.exec_()

if __name__ == '__main__':
    main()

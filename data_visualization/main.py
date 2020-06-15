
import argparse
import pandas as pd

from PySide2.QtCore import QDateTime, QTimeZone
from PySide2.QtWidgets import QApplication
from main_window import MainWindow
from widgets import Widget

def transform_date(utc, timezone):
    utc_fmt = 'yyyy-MM-ddTHH:mm:ss.zzzZ'
    new_date = QDateTime().fromString(utc, utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date

def read_data(fname):
    df = pd.read_csv(fname)

    df = df.drop(df[df.mag < 0].index)
    magnitudes = df["mag"]

    timezone = QTimeZone(b'Europe/Berlin')

    times = df['time'].apply(lambda x: transform_date(x, timezone))

    return times, magnitudes

if __name__ == '__main__':
    options = argparse.ArgumentParser()
    options.add_argument('-f', '--file', type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)

    # Qt Application
    app = QApplication(sys.argv)

    widget = Widget(data)
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec_())
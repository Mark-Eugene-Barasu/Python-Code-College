from __future__ import annotations

from pathlib import Path
import csv
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt


def load_weather_data(csv_path: Path):
    """Load the death_valley weather CSV.

    Refactors parsing with try/except so missing/bad rows don't crash.
    Returns: (dates, highs, lows)
    """
    try:
        text = csv_path.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Could not find CSV at: {csv_path}\n"
            "Check that weather_data/death_valley_2021_simple.csv exists."
        ) from e

    lines = text.splitlines()
    reader = csv.reader(lines)

    try:
        next(reader)  # header
    except StopIteration as e:
        raise ValueError(f"CSV appears empty: {csv_path}") from e

    dates: list[datetime] = []
    highs: list[int] = []
    lows: list[int] = []

    for row_num, row in enumerate(reader, start=2):
        # Expected columns: 0.. , 2=date, 3=high, 4=low
        if len(row) < 5:
            print(f"Skipping row {row_num}: not enough columns")
            continue

        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
        except ValueError:
            print(f"Skipping row {row_num}: bad date '{row[2]}'")
            continue

        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing/invalid data for {current_date}")
            continue

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    return dates, highs, lows


def plot_highs_lows(dates, highs, lows) -> None:
    plt.style.use("ggplot")

    # Tkinter/Tcl backend can be broken in some environments.
    # If creating a GUI figure fails, force a safe backend and keep going.
    try:
        fig, ax = plt.subplots()
    except Exception:
        matplotlib.use("Agg", force=True)
        fig, ax = plt.subplots()

    ax.plot(dates, highs, color="red", alpha=0.5)
    ax.plot(dates, lows, color="blue", alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    ax.set_title(
        "Daily High and Low Temperatures, 2021\nDeath Valley, CA", fontsize=20)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    # If plt.show() can't open a window, save to disk instead.
    try:
        plt.show()
    except Exception:
        out_file = Path(__file__).resolve().parent / \
            "death_valley_highs_lows.png"
        fig.savefig(out_file, dpi=150, bbox_inches="tight")
        print(f"GUI display not available; saved plot to: {out_file}")


def main() -> None:
    csv_path = (
        Path(__file__).resolve().parent
        / "weather_data"
        / "death_valley_2021_simple.csv"
    )

    dates, highs, lows = load_weather_data(csv_path)
    if not dates:
        raise ValueError("No valid rows were parsed from the CSV.")

    plot_highs_lows(dates, highs, lows)


if __name__ == "__main__":
    main()

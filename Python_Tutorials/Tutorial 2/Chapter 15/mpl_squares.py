import os
import matplotlib

# Prefer GUI backend; if Tk/Tcl is broken, fall back to headless.
try:
    matplotlib.use("TkAgg")
except Exception:
    matplotlib.use("Agg")

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

chapter_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(chapter_dir, "mpl_squares.png")

plt.style.use("seaborn")

try:
    fig, ax = plt.subplots()
    ax.plot(input_values, squares, linewidth=3)

    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)
    ax.tick_params(labelsize=14)

    plt.show()
except Exception:
    # TkAgg can fail at runtime due to missing Tcl (e.g., init.tcl). Save instead.
    matplotlib.use("Agg", force=True)
    import matplotlib.pyplot as plt2

    fig, ax = plt2.subplots()
    ax.plot(input_values, squares, linewidth=3)

    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)
    ax.tick_params(labelsize=14)

    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved plot to: {out_path}")

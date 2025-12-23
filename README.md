# Chebyshev Theorem Demo (Stats I Extra Credit)

This project is a simple extra credit assignment for my **Statistics I** class. It demonstrates **Chebyshev’s Theorem** using a small Tkinter GUI and a Matplotlib visualization.

## What it does
- Lets the user input:
  - a **k-value**
  - a list of **population data points** (space-separated)
    
- Computes:
  - the **population mean** (μ)
  - the **population standard deviation** (σ)
  - the interval **μ ± kσ**
  - the **actual percentage** of data points that fall within that interval
  - Chebyshev’s guaranteed minimum percentage:  
    $$1 - \frac{1}{k^2}$$
 
- Displays a simple number-line style plot showing:
  - the interval endpoints (**μ − kσ** and **μ + kσ**)
  - the data points on the line
  - the minimum guaranteed percentage vs. the actual percentage

## Files
- `chebyshev_gui.py` — Tkinter GUI for entering inputs and displaying the plot.
- `chebyshev_plot.py` — Calculates statistics and builds the Matplotlib figure used by the GUI.

## How to run
1. Make sure you have Python installed (3.x recommended).
2. Install Matplotlib if you don’t already have it:
   ```bash
   pip install matplotlib
3. Run:
   ```bash
   python chebyshev_gui.py

## Notes
- This demo assumes **population** when computing standard deviation and as such, the dataset input is treated as the full dataset.
- Chebyshev’s Theorem provides a **worst-case** lower bound, so the “minimum possible” percentage may be much lower than the actual percentage for a given dataset.

## Purpose
- The goal of this project is to provide a simple interactive way to see how Chebyshev’s bound compares to real data, and to visualize the interval **μ ± kσ** on a number line.

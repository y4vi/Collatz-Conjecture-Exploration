import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# ---------- Collatz logic ----------
def collatz_sequence(n, max_steps=5000):
    seq = [n]
    steps = 0
    while n != 1 and steps < max_steps:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
        steps += 1
    return seq


def collatz_steps(n, max_steps=5000):
    steps = 0
    while n != 1 and steps < max_steps:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


# ---------- UI ----------
st.set_page_config(page_title="Collatz Conjecture Explorer", layout="centered")

st.title("🔢 Collatz Conjecture Explorer")
st.write("Explore trajectories and stopping-time statistics of the Collatz conjecture.")

st.divider()

# ---------- Single number ----------
st.header("Single Number Trajectory")

n = st.number_input("Enter a number n > 1",
                    min_value=2,
                    value=27,
                    step=1)

if st.button("Plot Collatz Trajectory"):
    seq = collatz_sequence(n)
    x = np.arange(len(seq))

    fig, ax = plt.subplots()
    ax.plot(x, seq, linewidth=2)
    ax.set_yscale("log")
    ax.set_xlabel("Step")
    ax.set_ylabel("Value (log scale)")
    ax.set_title(f"Collatz Trajectory for n = {n}")
    ax.grid(True)

    st.pyplot(fig)

st.divider()

# ---------- Range statistics ----------
st.header("Step Frequency (Range Analysis)")

a = st.number_input("From ( > 1 )", min_value=2, value=2, step=1)
b = st.number_input("To ( > From )", min_value=3, value=100, step=1)

if st.button("Plot Step Frequency"):
    if a >= b:
        st.error("The upper bound must be greater than the lower bound.")
    else:
        values = range(int(a), int(b) + 1)
        steps = [collatz_steps(n) for n in values]

        fig, ax = plt.subplots()
        ax.hist(steps, bins=30)
        ax.set_xlabel("Number of steps to reach 1")
        ax.set_ylabel("Frequency")
        ax.set_title(f"Collatz Stopping-Time Distribution ({a} to {b})")
        ax.grid(True)

        st.pyplot(fig)

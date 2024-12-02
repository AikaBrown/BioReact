# BioReact: Dynamic Simulation of a Continuous Stirred Tank Bioreactor (CSTR)

BioReact is a Python-based simulation tool for modeling the dynamic behavior of a Continuous Stirred Tank Bioreactor (CSTR). It uses the fourth-order Runge-Kutta method to solve differential equations for biomass and substrate balances, incorporating Monod kinetics for microbial growth.

This repository is ideal for students, researchers, and engineers working in biotechnology, bioengineering, or process control.

---

## Features

- **Dynamic Simulation:**
  - Simulates biomass and substrate concentrations over time.
  - Tracks the specific growth rate (\( \mu \)) dynamically.
  
- **Phase Diagram:**
  - Generates a plot of biomass vs substrate concentration.

- **Growth and Consumption Analysis:**
  - Plots biomass and substrate concentrations as functions of time.
  - Visualizes the specific growth rate over time.

- **Customizable Parameters:**
  - Easily adjust reactor conditions, microbial kinetics, and simulation parameters.

---

Aquí tienes el contenido reescrito usando sintaxis compatible con MathJax y GitHub para renderizar correctamente las expresiones matemáticas:

---

### How It Works

The program solves the following equations for a CSTR:

**1. Biomass balance:**
$
\frac{dX}{dt} = X \cdot (\mu - D)
$

**2. Substrate balance:**
$
\frac{dS}{dt} = D \cdot (S_f - S) - \frac{\mu \cdot X}{Y}
$

**3. Growth rate (Monod model):**
$
\mu = \frac{\mu_{\text{max}} \cdot S}{K_s + S}
$

Where:

- $X$: Biomass concentration (g/L)
- $S$: Substrate concentration (g/L)
- $D$: Dilution rate ($F / V$) (1/h)
- $S_f$: Feed substrate concentration (g/L)
- $\mu$: Specific growth rate (1/h)
- $Y$: Biomass yield coefficient (g biomass/g substrate)
- $\mu_{\text{max}}$: Maximum specific growth rate (1/h)
- $K_s$: Substrate affinity constant (g/L)

---

## Getting Started

### Prerequisites

- Python 3.8 or later
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`

Install the required libraries using:
```bash
pip install numpy pandas matplotlib

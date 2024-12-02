Aquí está el README completo actualizado con las fórmulas matemáticas reescritas en formato MathJax compatible con GitHub:

---

# BioReact: Dynamic Simulation of a Continuous Stirred Tank Bioreactor (CSTR)

BioReact is a Python-based simulation tool for modeling the dynamic behavior of a Continuous Stirred Tank Bioreactor (CSTR). It uses the fourth-order Runge-Kutta method to solve differential equations for biomass and substrate balances, incorporating Monod kinetics for microbial growth.

This repository is ideal for students, researchers, and engineers working in biotechnology, bioengineering, or process control.

---

## Features

- **Dynamic Simulation:**
  - Simulates biomass and substrate concentrations over time.
  - Tracks the specific growth rate ($\mu$) dynamically.
  
- **Phase Diagram:**
  - Generates a plot of biomass vs substrate concentration.

- **Growth and Consumption Analysis:**
  - Plots biomass and substrate concentrations as functions of time.
  - Visualizes the specific growth rate over time.

- **Customizable Parameters:**
  - Easily adjust reactor conditions, microbial kinetics, and simulation parameters.

---

## How It Works

The program solves the following equations for a CSTR:

**1. Biomass balance:**
$$
\frac{dX}{dt} = X \cdot (\mu - D)
$$

**2. Substrate balance:**
$$
\frac{dS}{dt} = D \cdot (S_f - S) - \frac{\mu \cdot X}{Y}
$$

**3. Growth rate (Monod model):**
$$
\mu = \frac{\mu_{\text{max}} \cdot S}{K_s + S}
$$

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
```

---

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BioReact.git
   cd BioReact
   ```

2. Import the functions in your script or Jupyter Notebook:
   ```python
   from cstr_simulation import runge_kutta_4, plot_biomass_vs_substrate, plot_biomass_and_substrate_vs_time, plot_growth_rate_vs_time
   ```

3. Define your parameters and run the simulation:
   ```python
   # Example parameters
   initial_time = 0.0          # Initial time (hours)
   initial_biomass = 0.1       # Initial biomass concentration (g/L)
   initial_substrate = 20.0    # Initial substrate concentration (g/L)
   yield_coefficient = 0.5     # Biomass yield coefficient (g biomass/g substrate)
   step_size = 0.1             # Simulation step size (hours)
   mu_max = 0.4                # Maximum specific growth rate (1/h)
   Ks = 1.0                    # Substrate affinity constant (g/L)
   reactor_volume = 1.0        # Reactor volume (L)
   flow_rate = 0.1             # Feed flow rate (L/h)
   substrate_feed = 50.0       # Substrate concentration in feed (g/L)
   simulation_steps = 100      # Number of steps to simulate

   # Run simulation
   results = runge_kutta_4(
       time=initial_time,
       biomass=initial_biomass,
       substrate=initial_substrate,
       yield_factor=yield_coefficient,
       step_size=step_size,
       mu_max=mu_max,
       Ks=Ks,
       volume=reactor_volume,
       flow_rate=flow_rate,
       substrate_feed=substrate_feed,
       steps=simulation_steps,
   )

   # Display results
   print(results.head())

   # Generate plots
   plot_biomass_vs_substrate(results)
   plot_biomass_and_substrate_vs_time(results)
   plot_growth_rate_vs_time(results)
   ```

---

### Example Output

1. **Phase Diagram:**
   Biomass vs Substrate Concentration.

   ![Phase Diagram](images/phase_diagram.png)

2. **Biomass and Substrate vs Time:**
   ![Biomass and Substrate vs Time](images/biomass_substrate_time.png)

3. **Growth Rate vs Time:**
   ![Growth Rate vs Time](images/growth_rate_time.png)

---

## Repository Structure

```
BioReact/
│
├── cstr_simulation.py       # Core simulation and plotting functions
├── examples/
│   ├── example_run.py       # Example script demonstrating usage
│   └── example_notebook.ipynb # Example Jupyter Notebook
├── images/                  # Folder for example plot images
└── README.md                # Documentation
```

---

## Contributing

Contributions are welcome! If you have ideas for improvements or additional features, feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact
For questions or suggestions, feel free to contact:  
**Emiliano Balderas Ramírez**  
PhD Student at the Instituto de Biotecnología, UNAM  
Email: [ebalderas@live.com.mx](mailto:ebalderas@live.com.mx)  
Phone: +52 2221075693  


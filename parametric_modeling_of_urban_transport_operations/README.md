# Parametric Modeling of Urban Transport Operations

### Vector Calculus & Spatial Cost Simulation for Mexico City Trolleybus Line 2

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

## Executive Summary

**Parametric Modeling of Urban Transport Operations** is an applied mathematics project designed to estimate the continuous operational costs of public transport infrastructure. Traditional budgetary evaluations typically rely on static averages per kilometer, overlooking how physical geography affects mechanical wear and power consumption.

This project addresses that limitation by treating Mexico City's Trolleybus Line 2 (Pantitlán–Chapultepec corridor) as a parameterized curve in a two-dimensional plane. By evaluating a multivariable scalar field along this trajectory, the system calculates cumulative operational costs meter by meter, factoring in tight urban curves and elevated highway infrastructure.

The project features a **live interactive dashboard** that allows users to adjust operational variables and run instant sensitivity analyses on the spatial cost model.

---

## Project Documentation
For an in-depth review of the mathematical framework, line integral proofs, and data validation, please refer to the:
* **[Technical Report & Case Study (PDF)](./docs/Financial_and_Operational_Analysis_of_the_Mexico_City_Trolleybus_Network__Focus_on_Line.pdf)**

---

## Core Technical Challenges

* **Geospatial to Metric Conversion:** How can angular latitudinal and longitudinal coordinate displacements be converted into highly accurate physical distances over a curved surface?
* **Line Integral Discretization:** How do we transition a continuous multivariable cost density function into a robust numerical integration pipeline?
* **Numerical Stability:** How can we computationally verify that our algorithmic approximation converges reliably using dyadic partitions and Riemann sums?

---

## Tech Stack

| Category | Tools / Methods |
|---|---|
| Data Engineering | Python, Pandas, NumPy |
| Mathematical Framework | Line Integrals, Scalar Fields, Haversine Formula, Riemann Sums |
| Interface & Visualization | Streamlit |
| Version Control | Git |

---

## Project Architecture

```bash
├── data/
│   └── coordinates.csv         # Geographic nodes of Trolleybus Line 2
│
├── docs/
│   └── Financial_and_Operational_Analysis_of_the_Mexico_City_Trolleybus_Network__Focus_on_Line.pdf  # Technical paper
│
├── app.py                      # Interactive Streamlit dashboard
├── cost_model_analysis.ipynb   # Step-by-step computational process & proof
└── README.md                   # Project overview
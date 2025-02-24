from fpdf import FPDF

# Create a new PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Content of the detailed summary for Unit 4: Thermal Physics
thermal_physics_content = """
Unit 4: Thermal Physics - Detailed Summary

Thermodynamics and Energy
- Definition: The study of energy, energy transformations, and its relation to matter.
- Key Conservation Principles:
  1. Conservation of Mass: Matter is neither created nor destroyed.
  2. Conservation of Energy (First Law of Thermodynamics): Total energy remains constant but can change forms.

Four Laws of Thermodynamics
1. Zeroth Law:
   - Defines thermal equilibrium and the concept of temperature.
   - States that if two systems are in thermal equilibrium with a third system, they are in thermal equilibrium with each other.
   - Practical Application: Use of thermometers to measure temperature.

2. First Law:
   - Energy cannot be created or destroyed; it can only transform between heat (Q) and work (W).
   - Equation: ΔU = Q - W, where ΔU is the change in internal energy.
   - Applications: Steam engines, heat pumps, and refrigeration systems.

3. Second Law:
   - Entropy (S) of an isolated system always increases during a spontaneous process.
   - Heat flows from hot to cold spontaneously and not the reverse.
   - Applications: Efficiency limits in heat engines and refrigerators.
   - Entropy Relation: ΔS = Q / T.

4. Third Law:
   - At absolute zero (0 K), the entropy of a perfect crystal is zero.
   - Absolute zero is unattainable due to the infinite operations required to achieve it.

Heat Transfer Mechanisms
1. Conduction:
   - Transfer of energy through particle interactions in solids.
   - Governing Law: Fourier’s Law (Q = -kA ΔT / x).
   - Applications: Thermal insulation, heat transfer in compound materials.
   
2. Convection:
   - Heat transfer in fluids due to bulk movement.
   - Examples: Sea and land breezes.

3. Radiation:
   - Heat transfer through electromagnetic waves.
   - Governing Laws: Stefan-Boltzmann Law, Kirchhoff’s Law, Wien’s Law.

Thermal Expansion
1. Linear Expansion:
   - Change in length (ΔL) of solids with temperature.
   - Equation: ΔL = α L₀ ΔT.

2. Volumetric Expansion:
   - Change in volume (ΔV) due to temperature.
   - Equation: ΔV = β V₀ ΔT.
   - Engineering Applications: Expansion joints in bridges and pipelines.

Steady-Flow Processes
- Describes systems with constant mass and energy flow over time.
- Examples:
  - Turbines, pumps, boilers, and heat exchangers.
  - Power plants and refrigeration systems.

Properties and Measurements
1. System Properties:
   - Intensive Properties: Independent of mass (e.g., temperature, pressure).
   - Extensive Properties: Dependent on mass (e.g., volume, energy).
   - Specific Properties: Extensive properties per unit mass.

2. Equilibrium States:
   - Thermal, mechanical, chemical, and phase equilibria.

3. Temperature Scales:
   - Kelvin Scale (SI system).
   - Rankine Scale (English system).
   - Celsius and Fahrenheit Scales: Based on freezing and boiling points of water.

4. Pressure Measurements:
   - Absolute pressure: Relative to a vacuum.
   - Gauge pressure: Difference from atmospheric pressure.
   - Measured using devices like barometers.

Additional Applications
- Thermal Insulation: Minimizing heat transfer in buildings.
- Formation of Ice on Ponds: Explained through heat conduction.
- Latent Heat:
  - Heat of Fusion: Energy to change solid to liquid.
  - Heat of Vaporization: Energy to change liquid to vapor.

This detailed summary provides a comprehensive overview of the fundamental concepts of thermal physics, including thermodynamic principles, heat transfer mechanisms, and their applications in engineering and natural processes.
"""

# Add the content to the PDF
for line in thermal_physics_content.split("\n"):
    pdf.multi_cell(0, 10, line)

# Save the PDF file
pdf_output_path = r"C:\Users\ASUS\OneDrive\Desktop\physics\Thermal_Physics_Detailed_Summary.pdf"
pdf.output(pdf_output_path)

pdf_output_path




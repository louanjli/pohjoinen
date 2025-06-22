"""
Magnetic North — Visualising Global Runway Magnetic Deviation

Author: Mohamed Louanjli
Year: 2025
Created for: MUU Helsinki Contemporary Art Centre – Open Call 2026 “Missä on pohjoinen” / “Where is the North”
Medium: Python-generated SVG visualisation, projected on canvas (300 × 150 cm)

Description:
This script processes open runway and airport data from OurAirports and estimates magnetic headings using a simplified
declination model. The output is an SVG drawing where each line represents a runway oriented according to its magnetic heading.
The visual metaphor draws on compass behaviour to explore themes of orientation, migration, and symbolic geography.

Dependencies:
- pandas
- svgwrite
- math
- (Data files: runways.csv, airports.csv)

Licensing:
- Code: MIT License
- Artwork: CC BY-NC-SA 4.0
See LICENSE and NOTICE.md for more details.
"""

"""
Generate SVG of magnetic runway headings only, using extended runway dataset
Author: Mohamed Louanjli
"""

import pandas as pd
import svgwrite
import math

# --- Load data ---
runways = pd.read_csv("data/runways.csv").dropna(subset=["le_latitude_deg", "le_longitude_deg", "le_heading_degT"])

# --- Parameters ---
width, height = 3000, 1500  # 2:1 canvas ratio

# --- Dummy declination function ---
def dummy_declination(lat, lon):
    # Placeholder: returns simplified declination model
    return -2.5 + (lon / 72.0)  # crude approximation for demo purposes

# --- Coordinate mapping ---
def latlon_to_xy(lat, lon):
    x = (lon + 180) * (width / 360)
    y = (90 - lat) * (height / 180)
    return x, y

# --- Draw heading as a short visible vector ---
def draw_heading(dwg, x, y, heading, length, colour):
    angle_rad = math.radians(heading)
    dx = length * math.sin(angle_rad)
    dy = -length * math.cos(angle_rad)
    dwg.add(dwg.line(start=(x, y), end=(x + dx, y + dy), stroke=colour, stroke_width=0.3))

# --- Create SVG ---
svg_path = "runway_magnetic_headings_maximum.svg"
dwg = svgwrite.Drawing(svg_path, size=(f"{width}px", f"{height}px}"))
dwg.add(dwg.rect(insert=(0, 0), size=(f"{width}px", f"{height}px"), fill='white'))

# --- Draw all magnetic headings ---
for _, row in runways.iterrows():
    lat = row['le_latitude_deg']
    lon = row['le_longitude_deg']
    heading_true = row['le_heading_degT']
    decl = dummy_declination(lat, lon)
    heading_mag = heading_true + decl

    x, y = latlon_to_xy(lat, lon)
    draw_heading(dwg, x, y, heading_mag, 5, 'red')

# --- Save file ---
dwg.save()

# Magnetic North — Visualising Global Runway Magnetic Deviation

**Author**: Mohamed Louanjli  
**Year**: 2025  
**Created for**: MUU Helsinki Contemporary Art Centre – Open Call 2026  “Missä on pohjoinen” / “Where is the North”
**Medium**: SVG animation and canvas projection (300 × 150 cm)

## Description

This artwork visualises the magnetic orientation of 15,249 real-world runways across the globe. It uses data from the OurAirports open data repository and incorporates magnetic declination values derived from NOAA’s World Magnetic Model (WMM). Each red line represents a runway, animated to sway like a compass needle before settling on its final magnetic heading.

The piece reflects on themes of orientation, migration, and the constructed mythology of the North. Inspired by the MUU 2026 open call and Rosa Liksom’s manuscript *Missä on pohjoinen* (“Where is the North”), this installation considers how the idea of the North functions as both a direction and a projection — magnetic, symbolic, and never entirely aligned.

## Development Notes

- The SVG data was generated using a custom Python script: [`magnetic_runway_headings_only.py`](magnetic_runway_headings_only.py)
- The script uses:
  - `pandas` for parsing and managing CSV datasets
  - `math` for trigonometric computation of headings
  - `svgwrite` to export clean vector linework
- Final animation is written in plain HTML/CSS/JavaScript
  - Uses SVG `<line>` elements
  - `stroke-dashoffset`, `transform`, and `opacity` animations
  - No external libraries required

## Data Sources

- **Runways and airports**:  
  © [OurAirports](https://ourairports.com/data/)  
  Licensed under [Open Data Commons Public Domain Dedication and License (PDDL)](https://opendatacommons.org/licenses/pddl/)

- **Magnetic declination model**:  
  [NOAA World Magnetic Model](https://www.ncei.noaa.gov/products/world-magnetic-model/software-and-coefficients-windows)

## Licensing

- **Code**: MIT License (see [`LICENSE`](LICENSE))
- **Artwork & animation**:  
  Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International  
  (see [`NOTICE.md`](NOTICE.md))

> Please consult the relevant files for full attribution and reuse conditions.

---

© 2025 Mohamed Louanjli. All rights reserved where applicable.

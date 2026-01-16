# Knit Beanie Size Grading Automation Tool 🧶🧢

A Python tool that automates realistic size grading (XS–XL) for knit beanies and hats,  
with estimated yarn length calculation and clean, professionally formatted Excel output.

Designed for real-world use by technical designers, knitwear developers, sampling teams  
and small-scale manufacturers working on cold-weather accessories.

**Current production version:** 0.1.0 (Jan 2026)

## 🌍 Project Overview

Creating consistent size runs for knit headwear is time-consuming and error-prone when done manually.  
This tool takes your base measurements, applies common industry grading increments, estimates realistic yarn requirements per size,  
and produces a clean Excel file ready for tech packs, sampling sheets or supplier communication.

The tool helps you:
- Generate full size ranges quickly and consistently
- See estimated yarn usage early in development
- Get automatic visual warnings for potentially problematic sizes
- Save many hours of repetitive spreadsheet work

## 🔢 Size Grading Summary

| Size | Crown Circumference (cm) | Height / Length (cm) | Brim Width (cm) | Gauge | Est. Yarn Length (m) | Notes                  |
|------|---------------------------|----------------------|-----------------|-------|----------------------|------------------------|
| XS   | 48.0                      | 20.0                 | 8.0             | 22    | 14.4                 | Potentially too small  |
| S    | 52.0                      | 21.0                 | 8.0             | 22    | 16.3                 |                        |
| M    | 56.0                      | 22.0                 | 8.0             | 22    | 18.3                 |                        |
| L    | 60.0                      | 23.0                 | 8.5             | 22    | 20.3                 |                        |
| XL   | 64.0                      | 24.0                 | 9.0             | 22    | 22.4                 | Potentially too large  |

⚠️ **Important:** Grading increments and yarn estimates are based on common knitwear industry practices.  
Actual results may vary depending on stitch pattern, yarn type, tension and blocking method.

## 🧠 Core Grading & Calculation Logic

**Model Type:** Geometric progression + simplified yarn estimation  
**Input Type:** Base measurements + stitch gauge

Base parameters you can customize:
- Base crown circumference (cm)
- Base total height / length (cm)
- Base brim / cuff width (cm)
- Base gauge (stitches per 10 cm)

Yarn length is estimated using simplified cylindrical + crown volume approximation  
(accurate enough for early-stage planning and material ordering).

The Notes column automatically flags potentially problematic sizes.

## 📊 Excel Output Features

What you get in the generated file:
1. Clean table layout with all sizes
2. Bold header row
3. Automatically adjusted column widths
4. Conditional formatting on Notes column  
   • Red background → Potentially too small  
   • Yellow background → Potentially too large
5. Custom filename support via --output flag

Sample output file included: examples/knit_beanie_graded_specs.xlsx

## ▶️ Running the Tool

1. Install from GitHub  
   pip install git+https://github.com/Xhenzouu/beanie-size-grader.git

2. Run with default base measurements (M = 56 cm circ)  
   beanie-grader

3. Run with custom base measurements  
   beanie-grader --base_circumference 54 --base_height 20 --base_brim 7 --base_gauge 22 --output my_beanie.xlsx

## 🛠️ Tech Stack (Updated Jan 2026)

- Python 3.8+  
- Click (CLI interface)  
- Pandas + Openpyxl (Excel generation & formatting)  
- Cross-platform compatibility

## ☁️ No Cloud Required

Fully local tool.  
No database, no internet connection, no external services needed.

## 🤝 Contributing

Pull requests welcome!

Please:
- ❌ Do not commit large test files or generated Excel outputs  
- 🔒 Respect the intended use case (technical knitwear development)  
- Consider contributing alternative grading rules or hat styles

Made with care for knitwear designers and makers who want faster, cleaner size development workflows 🧡

January 2026
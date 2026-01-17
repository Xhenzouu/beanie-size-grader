# Knit Size Grading Automation Tool 🧶👕

A Python tool that automates **realistic size grading** for knit beanies, hats, and other apparel,  
with **config-driven measurements**, estimated material usage, and clean, professionally formatted Excel output.

Designed for **technical designers, knitwear developers, sampling teams**, and **small-scale manufacturers** working on cold-weather accessories or garments.

**Current production version:** 0.2.0 (Jan 2026)

---

## 🌍 Project Overview

Manual size grading for multiple products is **time-consuming and error-prone**.  
This tool allows you to:

- Load product-specific configurations from **YAML files**
- Generate full size ranges quickly and consistently
- See **estimated yarn or fabric usage** early in development
- Get **automatic warnings for potentially problematic sizes**
- Save hours of repetitive spreadsheet work

**Multi-product support** means the same engine can now handle:
- Knit beanies and hats
- T-shirts, sweaters, or other garments  
- Any product defined via a config YAML

---

## 🔢 Size Grading Summary (Example: Beanies)

| Size | Crown Circumference (cm) | Height / Length (cm) | Brim Width (cm) | Gauge | Est. Yarn Length (m) | Notes                  |
|------|---------------------------|----------------------|-----------------|-------|----------------------|------------------------|
| XS   | 48.0                      | 20.0                 | 8.0             | 22    | 14.4                 | Potentially too small  |
| S    | 52.0                      | 21.0                 | 8.0             | 22    | 16.3                 |                        |
| M    | 56.0                      | 22.0                 | 8.0             | 22    | 18.3                 |                        |
| L    | 60.0                      | 23.0                 | 8.5             | 22    | 20.3                 |                        |
| XL   | 64.0                      | 24.0                 | 9.0             | 22    | 22.4                 | Potentially too large  |

> ⚠️ Grading increments and yarn estimates are based on common industry practices.  
> Actual results may vary depending on stitch pattern, yarn/fabric type, tension, or blocking.

---

## 🧠 Core Grading & Calculation Logic

**Model Type:** Geometric progression + simplified material estimation  
**Input Type:** Config-driven base measurements per product

- Product measurements and sizes are **defined in YAML** files (`configs/`)  
- Base parameters can be overridden via CLI flags if needed  
- Material usage (yarn/fabric) is **estimated using geometric approximations**  
- Notes column automatically flags potential sizing issues

---

## 📊 Excel Output Features

Generated files now include:

1. **Graded Specs sheet** with all sizes
2. Bold header row
3. Automatically adjusted column widths
4. Conditional formatting:
   - Red → Potentially too small  
   - Yellow → Potentially too large
5. **Summary sheet**:
   - Counts per size
   - Highlights XS/XL (or first/last sizes)
6. Custom output filename support via `--output` flag

---

## ▶️ Running the Tool

### 1️⃣ Install

```bash
pip install git+https://github.com/Xhenzouu/beanie-size-grader.git

2️⃣ Run grading for a product (default example)

beanie-grader run --config configs/beanie.yaml

3️⃣ Run grading with custom output filename

beanie-grader run --config configs/beanie.yaml --output my_beanie.xlsx

4️⃣ Validate a product config

beanie-grader validate --config configs/shirt.yaml

✅ Ensures the YAML structure is correct without generating Excel output

🛠️ Tech Stack

Python 3.8+
Click / argparse CLI interface
Pandas + Openpyxl (Excel generation & formatting)
PyYAML (configuration loading)
Cross-platform support (Windows / macOS / Linux)

☁️ Fully Local

No cloud required
No database or external service needed

🤝 Contributing

Pull requests welcome! Consider contributing:

Alternative grading rules
New product configs (YAML)
Excel formatting improvements

Please avoid committing large test files or generated Excel outputs.

Made with care for designers and makers who want faster, cleaner size development workflows 🧡

🆕 Highlights in v0.2.0

Multi-product support via YAML configs (configs/)
CLI redesign with subcommands: run and validate
Excel summary sheet with size counts and conditional highlights
Fully refactored engine (engine.py) and helpers (utils.py)
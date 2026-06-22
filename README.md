# NatProCP

**A Plant-Derived Natural Products Database for Crop Protection Targeting SDH1 Protein of *Magnaporthe oryzae***

NatProCP is a curated, large-scale database of **2,660 plant-derived natural products** from **262 plant species**, systematically compiled and characterized for agricultural pest and disease management. The database is designed to support virtual screening, binding affinity prediction, and discovery of natural fungicides against *Magnaporthe oryzae* — the causative agent of rice blast, one of the world's most destructive crop diseases.

The database integrates **40 molecular and pharmacological properties** for each compound, including drug-likeness metrics (Lipinski violations, Ghose violations, bioavailability), ADMET profiles (absorption, distribution, metabolism, excretion, toxicity), CYP inhibition profiles, and toxicity predictions. Every compound is linked to literature references and paired with 3D structural models (PDB format) for structure-based virtual screening.

**Original developer:** Nimai Mahanida
**Contributors:** Mohit Kumar, Satyaranjan Biswal

---

## Overview

Fungal diseases cause an estimated **10–16% loss** in global crop yields annually. *Magnaporthe oryzae* alone accounts for massive economic damage in rice-growing regions. Synthetic fungicides are effective but face resistance evolution and environmental concerns. Natural products offer a rich source of bioactive scaffolds with diverse mechanisms, lower resistance risk, and regulatory acceptance for organic and integrated pest management (IPM).

NatProCP addresses the discovery bottleneck by providing:

1. **Comprehensive chemical space** — 2,660 molecules from proven medicinal plants, each with **recorded ethnobotanical/agricultural use**.
2. **Pre-computed molecular properties** — enabling rapid similarity searches, ADMET filtering, and machine-learning-based binding affinity ranking without expensive docking.
3. **Organized by plant source** — 262 species grouped for ethnobotanical exploration and species-level validation.
4. ** 3D structural models** — PDB-formatted atomic coordinates for every compound, enabling structure-based docking and molecular dynamics simulations.
5. **Web-based interactive interface** — search, browse, visualize, and download compounds and their properties with a single click.

---

## Database structure

### Compound dataset

**Total compounds:** 2,660  
**Plant species:** 262  
**Fields per compound:** 40 molecular/pharmacological descriptors

#### Core identifiers

| Field | Description |
|---|---|
| Compound Name | Chemical/IUPAC name |
| PubChem ID | Link to PubChem record for cross-validation |
| Common Name | Vernacular name(s) |
| Scientific Name | Plant species source |
| References | Citation(s) for isolation/characterization |

#### Molecular descriptors (RDKit-derived)

| Property | Description |
|---|---|
| SMILES | Canonical SMILES notation for structure |
| Formula | Molecular formula |
| MW | Molecular weight (g/mol) |
| Rotatable bonds | Count of rotatable bonds |
| H-bond acceptors | HBA (Lipinski) |
| H-bond donors | HBD (Lipinski) |
| MR | Molar refractivity |
| TPSA | Topological polar surface area (Ų) |

#### Lipophilicity and solubility

Calculated using multiple methods to capture consensus predictions:

| Property | Source |
|---|---|
| iLOGP | Wildman–Crippen logP |
| XLOGP3 | XLOGP3 descriptor |
| WLOGP | Wildman–Crippen descriptor |
| MLOGP | Moriguchi logP |
| Consensus Log P | Mean of all methods |
| Log S | Water solubility prediction |

#### ADMET and drug-likeness

| Property | Description |
|---|---|
| GI absorption | Predicted good gastrointestinal absorption (Yes/No) |
| BBB permeant | Blood–brain barrier penetration (Yes/No) |
| CYP1A2 inhibitor | Predicted CYP1A2 inhibition (Yes/No) |
| CYP2C19 inhibitor | Predicted CYP2C19 inhibition (Yes/No) |
| CYP2C9 inhibitor | Predicted CYP2C9 inhibition (Yes/No) |
| CYP2D6 inhibitor | Predicted CYP2D6 inhibition (Yes/No) |
| CYP3A4 inhibitor | Predicted CYP3A4 inhibition (Yes/No) |
| Lipinski violations | Count of rule-of-five violations |
| Ghose violations | Count of Ghose drug-likeness violations |
| Bioavailability Score | Overall predicted bioavailability (0–1 scale) |
| PAINS alerts | Matched pan-assay interference compounds |

#### Toxicity predictions

| Property | Description |
|---|---|
| AMES Toxicity | Predicted mutagenicity (Yes/No) |
| Max. Tolerated Dose (human) | Predicted MTD in mg/kg |
| hERG I Inhibitor | Predicted human Ether-a-go-go–related gene inhibition (high-risk) |
| hERG II Inhibitor | Predicted hERG inhibition (low-risk) |
| Oral Rat Acute Toxicity (LD50) | Predicted acute oral toxicity in mg/kg |
| Oral Rat Chronic Toxicity (LOAEL) | Predicted chronic LOAEL in mg/kg |
| Hepatotoxicity | Predicted liver toxicity (Yes/No) |
| Skin Sensitisation | Predicted dermal sensitization (Yes/No) |
| T. Pyriformis Toxicity | Predicted protozoan toxicity (Yes/No) |
| Minnow Toxicity | Predicted aquatic toxicity (Yes/No) |

### File organization

```
NaturePro/
├── data.csv                    # Master compound table (2,660 compounds, 40 columns)
├── csv_data/                   # Plant-species-organized data
│   ├── Abutilon indicum/
│   ├── Acacia catechu/
│   ├── ... (262 species total)
│   └── Zingiber officinale/
├── pdb/                        # 3D structures for all compounds (PDB format)
│   ├── 1.pdb
│   ├── 2.pdb
│   ├── ... 
│   └── 2660.pdb
├── assets/                     # Pre-compiled molecule sets and web resources
│   ├── all_compounds.pdb       # Combined PDB (13 MB)
│   ├── all_compounds.sdf       # Combined SDF (17 MB)
│   ├── antifungal.sdf          # Filtered antifungal set (6 MB)
│   ├── antiviral.sdf           # Filtered antiviral set (4.1 MB)
│   ├── ICAR_Data_Use_Licence.pdf
│   ├── about_database.html
│   ├── about_us.html
│   └── ... (image assets)
├── app.py                      # Dash web interface
├── requirements.txt
└── 126.pdb, 126.sdf            # Example structures
```

### Species representation

The 262 plant species span traditional crop-protection plants and ethnobotanically documented anti-fungal species:

**Top 5 by compound count:**
1. *Phyllanthus emblica* — 164 compounds
2. *Zingiber officinale* — 159 compounds
3. *Piper longum* — 83 compounds
4. *Vitex negundo* — 81 compounds
5. *Mangifera indica* — 81 compounds

All species are recorded with their common names and scientific nomenclature to enable cross-validation and ethnobotanical exploration.

---

## Molecular properties and rationale

Each descriptor serves a specific screening goal:

| Goal | Properties used |
|---|---|
| **Similarity search** | Molecular formula, MW, SMILES, LogP |
| **ADMET filtering** | GI absorption, BBB permeant, CYP inhibition, solubility (Log S) |
| **Toxicity profiling** | AMES, MTD, hERG, hepatotoxicity, skin sensitization, aquatic toxicity |
| **Drug-likeness** | Lipinski violations, Ghose violations, bioavailability score, PAINS |
| **Binding potential** | MW, TPSA, H-bond donors/acceptors, rotatable bonds (predictive of binding affinity) |

These 40 properties enable filtering of the compound set to **low-toxicity, high-bioavailability molecules** before virtual screening against *Magnaporthe oryzae* SDH1.

---

## Standalone data access

### Main dataset (`data.csv`)

All 2,660 compounds in one CSV file, ready for import into Python, R, or spreadsheet software:

```bash
# Python
import pandas as pd
df = pd.read_csv('data.csv')
print(df.shape)           # (2660, 40)
print(df.columns.tolist())
```

### Plant-specific subsets

Each plant species has its own CSV in `csv_data/SPECIES_NAME/data.csv`:

```bash
# Compounds from Ginger (Zingiber officinale)
ginger_df = pd.read_csv('csv_data/Zingiber officinale/data.csv')
print(ginger_df.shape)  # (159, 40)
```

### Pre-compiled structure files

- **`all_compounds.pdb`** — Complete set of 2,660 structures in one file (13 MB)
- **`all_compounds.sdf`** — Complete set in SDF format (17 MB)
- **`antifungal.sdf`** — Subset pre-filtered for antifungal properties (6 MB)
- **`antiviral.sdf`** — Subset pre-filtered for antiviral properties (4.1 MB)

Individual PDB files are indexed by compound ID in `pdb/1.pdb`, `pdb/2.pdb`, ..., `pdb/2660.pdb`.

---

## Web interface

A Dash-based interactive application provides a point-and-click interface to the database:

### Features

1. **Plant / crop selector** — Dropdown menu to browse compounds by plant species.
2. **Compound search** — Query by compound name or PubChem ID.
3. **Properties table** — Display all 40 molecular and toxicity descriptors for selected compound.
4. **3D structure visualization** — Interactive molecular viewer using dash-bio (rotate, zoom, inspect atoms).
5. **Bulk downloads** — Export species data, all structures, or pre-filtered antifungal/antiviral sets.
6. **About pages** — Database rationale, data sources, licensing, team information.

### Running the web app

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py

# Open in browser
http://127.0.0.1:8050
```

For production deployment:

```bash
gunicorn app:server
```

---

## Integration with binding affinity prediction

NatProCP is the **reference screening library** for the companion **ML-VSPred** tool — a machine-learning model for predicting protein–ligand binding affinity. The 2,660 compounds in NatProCP serve as the **default virtual screening set** (`dpnp_ligand_features.csv` in ML-VSPred), enabling rapid ranking of all plant-derived compounds against a user-supplied protein target (e.g., *M. oryzae* SDH1).

**Workflow:**
1. Upload *M. oryzae* SDH1 PDB structure to ML-VSPred.
2. ML-VSPred automatically ranks all 2,660 NatProCP compounds by predicted binding affinity.
3. Download ranked list and select top candidates for experimental validation or docking refinement.

---

## Data quality and validation

### Curation process

- **Source verification**: All compounds sourced from peer-reviewed literature and natural product databases (ChEMBL, UNPD).
- **Structure validation**: SMILES and 3D coordinates validated using RDKit and OpenBabel.
- **Property consistency**: Calculated properties cross-validated against known compounds.

### Molecular property calculation

All 40 descriptors are computed using industry-standard tools:

- **RDKit** — Lipinski properties, molecular descriptors
- **ADMET SAR** — ADMET and toxicity predictions
- **PaDEL-Descriptor** — Additional molecular descriptors
- **PubChem** — Cross-validation and alternative property sources

### Coverage

- **100% structure coverage**: Every compound has a 3D model
- **100% property coverage**: All 40 descriptors calculated for all 2,660 compounds
- **Reference completeness**: Literature citations for >95% of compounds

---

## Usage examples

### Example 1: Find all ginger compounds with good oral bioavailability

```python
import pandas as pd

df = pd.read_csv('csv_data/Zingiber officinale/data.csv')

# Filter: Lipinski-compliant, low toxicity, good GI absorption
filtered = df[
    (df['Lipinski violations'] == 0) &
    (df['GI absorption'] == 'High') &
    (df['Hepatotoxicity'] == 'No')
]

print(f"Compounds meeting criteria: {len(filtered)}")
print(filtered[['Compound Name', 'MW', 'LogP', 'TPSA']])
```

### Example 2: Rank compounds by predicted safety profile

```python
# Lower MTD = lower toxicity. Sort ascending for safest compounds.
safe_compounds = df.sort_values('Max. Tolerated Dose(human)', ascending=True)
print(safe_compounds[['Compound Name', 'Max. Tolerated Dose(human)']].head(10))
```

### Example 3: Virtual screening against M. oryzae SDH1

```python
# Use ML-VSPred (separate repo) to predict binding affinity
# 1. Load NatProCP data.csv
# 2. Upload SDH1.pdb from M. oryzae
# 3. ML-VSPred computes binding affinity for all 2,660 compounds
# 4. Download ranked list

# Then filter results by ADMET safety
screening_results = pd.read_csv('ml_vspred_output.csv')
high_affinity_safe = screening_results[
    (screening_results['Binding_Affinity'] > 7.0) &  # Strong predicted binding
    (results['Hepatotoxicity'] == 'No') &
    (results['Lipinski violations'] == 0)
]
print(high_affinity_safe)
```

### Example 4: Explore plant-specific chemistry

```python
import matplotlib.pyplot as plt

# Load multiple species
species_list = ['Zingiber officinale', 'Curcuma longa', 'Piper longum']
mw_by_species = {}

for species in species_list:
    df = pd.read_csv(f'csv_data/{species}/data.csv')
    mw_by_species[species] = df['MW'].mean()

# Plot average molecular weight by species
plt.bar(mw_by_species.keys(), mw_by_species.values())
plt.ylabel('Mean Molecular Weight')
plt.xticks(rotation=45)
plt.show()
```

---

## File formats

### CSV format

Standard comma-separated values, UTF-8 encoded. Compatible with Excel, R, Python pandas, and all statistical software.

**Example row:**
```
(R)-N-(1′-Methoxycarbonyl-2′-phenylethyl)-4-hydroxybenzamide,73941365,Atibala,Abutilon indicum,PMID: 18636384,COC(=O)C(CC1=CC=CC=C1)NC(=O)C2=CC=C(C=C2)O,C17H17NO4,299.32,7,4,2,81.65,75.63,2.52,2.22,1.91,2.2,2.27,-3.04,High,No,No,No,No,No,No,0,0,0.55,0,No,-0.492,No,No,2.107,1.728,No,No,0.705,0.975
```

### PDB format

3D atomic coordinates in Protein Data Bank format, suitable for:
- Molecular visualization (PyMOL, Chimera, Jmol)
- Docking (AutoDock, GOLD, Glide)
- Molecular dynamics (AMBER, GROMACS)
- Descriptor calculation (CASTp, DSSP)

### SDF format

Structure data file format, compatible with:
- RDKit, OpenBabel, SMSD
- ChemAxon Marvin
- CDK (Chemistry Development Kit)

---

## System requirements

### For data access (minimal)

- Python 3.6+
- pandas
- Text editor or spreadsheet software

### For web interface

- Python 3.6+
- Dash >= 2.18.1
- pandas >= 2.2.3
- numpy >= 1.26.4
- Flask >= 3.0.3
- See `requirements.txt` for exact versions

### For structure processing

- RDKit
- OpenBabel
- BioPython

---

## Installation

```bash
git clone https://github.com/nimaibio/NaturePro.git
cd NaturePro

# Install web dependencies
pip install -r requirements.txt

# Run the web interface
python app.py
```

Then open `http://localhost:8050` in a web browser.

---

## License

The NatProCP database is released under the **ICAR Data Use License** (Indian Council of Agricultural Research). The database may be used for academic, research, and educational purposes with proper attribution. Commercial use requires explicit written permission from ICAR.

See `assets/ICAR_Data_Use_Licence.pdf` for full license text.

---

## Citation

If you use NatProCP in your research, please cite:

> Mahanida, N., Kumar, M., Biswal, S. *NatProCP: A Plant-Derived Natural Products Database for Crop Protection Targeting SDH1 Protein of Magnaporthe oryzae.* <!-- TODO: Journal, Year, Volume, DOI -->

---

## Complementary resources

- **ML-VSPred** — Companion machine-learning tool for binding affinity prediction against NatProCP compounds. Enables rapid virtual screening without docking. [GitHub](https://github.com/nimaibio/binding_affinity)

- **PubChem** — Cross-validation and literature search for each compound via PubChem ID.

- **ChEMBL** — Additional bioactivity and structure data for compounds in NatProCP.

- **TCMSP** — Traditional Chinese Medicine Systems Pharmacology Database, a related natural products resource with similar ADMET/toxicity annotations.

---

## Contact and support

For questions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/nimaibio/NaturePro).

**Lead developer:** Nimai Mahanida  
**Contributors:** Mohit Kumar, Satyaranjan Biswal  

<!-- TODO: Add emails, institutional affiliations, and ORCID IDs -->

---

## Acknowledgments

NatProCP was developed with support from [**TODO: Funding agency, institution, lab**]. We gratefully acknowledge the herbalists, farmers, and traditional knowledge keepers whose documented plant uses guided compound selection.

---

## Version history

- **v1.0** (June 2024) — Initial release: 2,660 compounds from 262 plant species, web interface, integrated into ML-VSPred pipeline.

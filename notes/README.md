# Probability & Statistics Framework Notes

This directory contains the "Ω-E Framework" book project files.

## Structure

- `part_iv/`: Generated Markdown files for Part IV (Case Dictionary).
- `iv_manifest.tsv`: The master ledger containing Question + Answer sets.
- `iv_lint.py`: Script to check the manifest for errors (TBDs, missing fields).
- `iv_gen.py`: Script to generate Markdown files from the manifest.

## Usage

1.  **Edit `iv_manifest.tsv`**: Add new entries.
    - Columns: `id`, `title`, `dom`, `obj`, `shape`, `etype`, `dec`, `dep`, `tool`, `src`, `q`, `a`, `given`, `assume`.
2.  **Lint**: Run `python3 iv_lint.py` to check for missing answers or invalid tags.
3.  **Generate**: Run `python3 iv_gen.py` to update/create Markdown files in `part_iv/`.

## Directory Mapping (Shape -> Folder)

- `shape/latent_obs` -> `A_latent_obs`
- `shape/standardize` -> `B_standardize`
- `shape/sampling` -> `C_sampling`
- `shape/sequence` -> `D_sequence`
- `shape/estimation` -> `E_estimation`
- `shape/hypothesis` -> `F_hypothesis`
- `shape/geometry` -> `G_geometry`

## Notes

- Symbols are standardized: Ω (U+03A9), H (Latent), O_i (Observation), q (Posterior), E (Event).
- The framework emphasizes "E-substitution" and "Sum/Product Decomposition".

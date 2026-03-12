# Changelog

## Environment and dependencies

- Added `pandas=1.5.2` to `conda_env.yml`.
- This keeps the environment compatible with the pinned `numpy=1.21.6` and avoids the pandas import failure caused by newer pandas releases.

## MuJoCo 3.x compatibility

- Removed the deprecated `collision="predefined"` attribute from `myoconverter/xml/template.xml`.
- Updated `myoconverter/optimization/utils/UtilsMujoco.py` to support both `eq_active` and `eq_active0` for equality constraints.
- Updated `myoconverter/optimization/utils/UtilsMujoco.py` to support all observed `actuator_moment` layouts:
  - dense 2D matrices
  - flattened dense arrays
  - MuJoCo 3.x sparse arrays reconstructed with `moment_rowadr`, `moment_rownnz`, and `moment_colind`

## Pipeline execution behavior

- Updated `myoconverter/conversion_steps/O2MSteps.py` so that when `convert=True`:
  - step 2 starts from the newly generated `cvt1` model
  - step 3 starts from the newly generated `cvt2` model
- This prevents stale `cvt2.xml` or `cvt3.xml` files from older MuJoCo versions from being reused accidentally.

## Windows multiprocessing and logging stability

- Updated `myoconverter/O2MPipeline.py` to handle `PermissionError` when an existing log file cannot be deleted because it is still in use.
- Updated `myoconverter/optimization/utils/UtilsForceOpt.py` to fall back to serial execution when `multiprocessing.Pool` is unavailable.
- This improves stability on Windows and in restricted execution environments.

## Safe example-script entry points

- Added `if __name__ == "__main__":` guards to the following files:
  - `examples/arm26.py`
  - `examples/gait10dof18musc.py`
  - `examples/gait23dof54musc.py`
  - `examples/leg6dof9musc.py`
  - `examples/neck6dof.py`
  - `examples/tug_of_war.py`
  - `examples/cli.py`
- This prevents Windows `spawn` child processes from re-running the full pipeline when importing these scripts.

## CLI argument parsing improvements

- Refactored `examples/cli.py` to use more standard `argparse` patterns.
- Renamed CLI flags to kebab-case:
  - `--osim-file`
  - `--geometry-folder`
  - `--output-folder`
  - `--convert-steps`
  - `--muscle-list`
  - `--generate-pdf`
  - `--add-ground-geom`
  - `--treat-as-normal-path-point`
- Replaced fragile list parsing with `nargs='+'` for:
  - `--convert-steps`
  - `--muscle-list`
- Replaced `type=bool` flags with paired boolean switches such as:
  - `--speedy` / `--no-speedy`
  - `--validation` / `--no-validation`
  - `--generate-pdf` / `--no-generate-pdf`

## Example comments and help text cleanup

- Standardized the docstrings, inline comments, and model-title comments across the example scripts.
- Fixed spelling and wording issues in the example files.
- Corrected the `generate_pdf` comments so they match the actual configuration values.
- Standardized the CLI help text in `examples/cli.py` to match the example-script wording.

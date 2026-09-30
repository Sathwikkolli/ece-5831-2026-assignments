# ECE 5831 (2026) - Assignment 2: NumPy Tutorial

Work through the [cs231n Python NumPy tutorial](https://cs231n.github.io/python-numpy-tutorial/),
written as a Jupyter Notebook in VS Code and run on Great Lakes with the `ece-5831-2026` conda environment.

| File | Content |
|---|---|
| `numpy-tutorials.ipynb` | The NumPy part of the cs231n tutorial, with every example run and its output saved |
| `README.md` | This file |

## Work completed

`numpy-tutorials.ipynb` follows the tutorial section by section:

| Section | What is covered |
|---|---|
| NumPy | Importing NumPy and checking the Python / NumPy versions |
| Arrays | `np.array`, rank and `shape`, `np.zeros`, `np.ones`, `np.full`, `np.eye`, `np.random.random`, plus `arange`, `linspace`, `reshape` |
| Array indexing | Slicing (and slices as views), mixing integer and slice indexing, integer array indexing, selecting/mutating one element per row, boolean array indexing |
| Data types | NumPy's `dtype` inference, forcing a `dtype`, converting with `astype`, bytes per element |
| Array math | Elementwise `+ - * /` and `np.add`, `np.subtract`, `np.multiply`, `np.divide`, `np.sqrt`; `dot` / `@` for vector and matrix products; `np.sum` with `axis`; other reductions; transpose `.T` |
| Broadcasting | Adding a vector to each row with a loop, with `np.tile`, and with broadcasting; the broadcasting rules; outer product, adding to rows and columns, scalar multiply; incompatible shapes; loop vs broadcasting timing |

## Run on Great Lakes

From the repository folder:

```bash
bash greatlakes_setup.sh
```

or run only this notebook:

```bash
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel_name=ece-5831-2026 A_02/numpy-tutorials.ipynb
```

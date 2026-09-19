#!/bin/bash
# One-shot setup for ECE 5831 on Great Lakes:
#   creates the ece-5831-2026 conda env, installs pandapower, registers the Jupyter kernel,
#   executes every notebook in place and runs python-tutorial-11.py.
# Usage (from the repo folder):  bash greatlakes_setup.sh
set -e
cd "$(dirname "$0")"
ENV=ece-5831-2026

# find conda: user's own Anaconda first, otherwise the Great Lakes anaconda module
if ! command -v conda >/dev/null 2>&1; then
    for d in "$HOME/anaconda3" "$HOME/miniconda3"; do
        [ -f "$d/etc/profile.d/conda.sh" ] && source "$d/etc/profile.d/conda.sh" && break
    done
fi
if ! command -v conda >/dev/null 2>&1; then
    MOD=$(module -t avail 2>&1 | grep -i anaconda | grep -i python3 | sort -V | tail -1)
    echo "Loading module $MOD"
    module load "$MOD"
fi
source "$(conda info --base)/etc/profile.d/conda.sh"
echo "Using conda: $(command -v conda)"

if conda env list | grep -q "^$ENV "; then
    echo "Environment $ENV already exists"
else
    conda create -y -n "$ENV" python=3.12
fi
conda activate "$ENV"
echo "Python: $(which python)"

pip install --upgrade pip
pip install "pandapower[all]" ipykernel nbconvert nbformat
python -m ipykernel install --user --name "$ENV" --display-name "Python ($ENV)"

for nb in ECE5831_lec_1/lec1_example_v1.ipynb learn-python-1.ipynb learn-python-2.ipynb \
          python-tutorial-1-10.ipynb python-tutorial-12-15.ipynb; do
    echo "=== executing $nb"
    jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel_name="$ENV" "$nb"
done

echo "=== running python-tutorial-11.py"
python python-tutorial-11.py > python-tutorial-11.out.txt
tail -3 python-tutorial-11.out.txt

echo
echo "All done. Environment: $ENV  |  Folder: $(pwd)"

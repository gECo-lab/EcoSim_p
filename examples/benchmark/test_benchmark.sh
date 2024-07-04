# Basic execution of benchmark model
# usage: benchmark.sh <model> <scenarios>
# model: models/model.json
# scenarios: scenarios/scenarios.json
# example: ,/benchmark.sh models/model.json scenarios/scenarios.json
#model=$1
#scenarios=$2

. venv


rm runs/*.csv

cd ../..

python3 ecosimp.py examples/benchmark/ config.json models/test_model.json scenarios/test_scenarios.json

cd examples/benchmark

quarto render "analisys/benchmark.qmd" --output-dir=../results 

xdg-open results/benchmark.html


# Basic execution of benchmark model
# usage: benchmark.sh <model> <scenarios>
# model: models/model.json
# scenarios: scenarios/scenarios.json
# example: ,/benchmark.sh models/model.json scenarios/scenarios.json
model=$1
scenarios=$2

. venv


rm runs/*.csv

cd ../..

python3 ecosimp.py examples/benchmark/ config.json $model $scenarios

cd examples/benchmark

#Rscript -e 'rmarkdown::render("benchmark.Rmd", output_format="html_document", output_dir="results")'

#sensible-browser results/benchmark.html&

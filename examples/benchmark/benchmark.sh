

rm runs/*.csv

cd ../..

python3 ecosimp.py examples/benchmark/ config.json model.json scenarios.json

cd examples/benchmark

Rscript -e 'rmarkdown::render("benchmark.Rmd", output_format="html_document", output_dir="results")'

sensible-browser results/benchmark.html&

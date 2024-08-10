
. venv

rm runs/*.csv

cd ../..

python3 ecosimp.py examples/ipd/ config.json "models/model_test_01.json" "scenarios/scenarios_test_01.json"

cd examples/ipd

Rscript -e 'rmarkdown::render("analisys/ipd.rmd", output_format="html_document", output_dir="results")'

#firefox results/ipd.html&
sensible-browser results/ipd.html&

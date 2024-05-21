model=$1
scenarios=$2

. venv

rm runs/*.csv

cd ../..

python3 ecosimp.py examples/ipd/ config.json "$model" "$scenarios"

cd examples/ipd

Rscript -e 'rmarkdown::render("analisys/ipd.rmd", output_format="html_document", output_dir="results")'

#firefox results/ipd.html&
sensible-browser results/ipd.html&

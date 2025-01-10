model=$1
scenarios=$2
kernel=$3
. venv

rm runs/*.csv

app_dir=$(pwd)

cd "$kernel"

python3 ecosimp.py "$app_dir" "$model" "$scenarios"

cd "$app_dir"

Rscript -e 'rmarkdown::render("analisys/ipd.rmd", output_format="html_document", output_dir="results")'

#firefox results/ipd.html&
sensible-browser results/ipd.html&
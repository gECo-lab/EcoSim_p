rm runs/*.csv

cd ../../kernel

python3 main.py ../examples/ipd/ config.json model.json scenarios.json

cd ../examples/ipd

Rscript -e 'rmarkdown::render("ipd.rmd", output_format="html_document", output_dir="results")'

#firefox results/ipd.html&
sensible-browser results/ipd.html&

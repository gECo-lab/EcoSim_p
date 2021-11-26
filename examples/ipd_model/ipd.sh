rm runs/*.csv

cd ../../kernel

python3 main.py ../examples/ipd_model/ ipd_config.json ipd.json

cd ../examples/ipd_model

Rscript -e 'rmarkdown::render("ipd.rmd", output_format="html_document", output_dir="results")'

#firefox results/ipd.html&
# sensible-browser results/ipd.html&

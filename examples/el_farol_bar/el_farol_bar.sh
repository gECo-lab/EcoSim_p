
cd ../../kernel

python3 main.py ../examples/el_farol_bar/ config.json model.json scenarios.json

cd ../examples/el_farol_bar

Rscript -e 'rmarkdown::render("El_Farol.rmd", output_format="html_document", output_dir="results")'

#firefox results/El_Farol.html &
# sensible-browser results/El_Farol.html &
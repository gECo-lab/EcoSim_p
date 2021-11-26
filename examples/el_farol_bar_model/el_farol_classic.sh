
cd ../../kernel

python3 main.py ../examples/el_farol_bar_model/ el_farol_bar_model_config.json el_farol_classic.json

cd ../examples/el_farol_bar_model

Rscript -e 'rmarkdown::render("El_Farol.rmd", output_format="html_document", output_dir="results")'

#firefox results/El_Farol.html &
# sensible-browser results/El_Farol.html &
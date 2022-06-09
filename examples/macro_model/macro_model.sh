
cd ../../kernel

python3 main.py ../examples/macro_model/ config.json model.json scenarios.json

cd ../examples/macro_model

Rscript -e 'rmarkdown::render("macro_model.rmd", output_format="html_document", output_dir="results")'

#firefox results/macro_Caiani.html
sensible-browser results/macro_model.html&


cd ../../kernel

python3 main.py ../examples/macro_model/ macro_model_config.json macro_Caiani.json

cd ../examples/macro_model

Rscript -e 'rmarkdown::render("macro_Caiani.rmd", output_format="html_document", output_dir="results")'

#firefox results/macro_Caiani.html
# sensible-browser results/macro_Caiani.html&

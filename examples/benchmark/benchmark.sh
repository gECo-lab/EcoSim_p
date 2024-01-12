
cd ../..

python3 ecosimp.py examples/benchmark/ config.json model.json scenarios.json

cd examples/benchmark

#Rscript -e 'rmarkdown::render("macro_model.rmd", output_format="html_document", output_dir="results")'

#firefox results/macro_Caiani.html
#sensible-browser results/macro_model.html&

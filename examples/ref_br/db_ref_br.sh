#mv runs/*.csv runs/previous_runs/.

cd ../../kernel

pdb3.8 main.py ../models/ref_br/ config.json model.json sceanarios.json

cd ../models/ref_br

#Rscript -e 'rmarkdown::render("ref_br.rmd", output_format="html_document", output_dir="results")'

#firefox results/ref_br.html&
#sensible-browser results/ref_br.html&


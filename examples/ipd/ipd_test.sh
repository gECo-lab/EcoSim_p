
. venv

rm runs/*.csv

app_dir=$(pwd)

kernel_dir=$"/home/rivero/Dropbox/Workspace_Current/Projects/Apps/EcoSim/EcoSim_p/main/EcoSim_p"

cd "$kernel_dir"

python3 ecosimp.py "$app_dir" "model_test_01.json" "scenarios_test_01.json"

cd /home/rivero/Dropbox/Workspace_Current/Projects/Apps/EcoSim/EcoSim_p/apps/ipd/ipd/

Rscript -e 'rmarkdown::render("analisys/ipd.rmd", output_format="html_document", output_dir="results")'

#firefox results/ipd.html&
sensible-browser results/ipd.html&

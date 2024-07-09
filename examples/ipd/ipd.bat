@echo off
setlocal

rem Set variables
set "model=%1"
set "scenarios=%2"

rem Activate the virtual environment
call venv\Scripts\activate

rem Remove CSV files from the runs directory
del /Q runs\*.csv

rem Navigate to the root directory
cd ..\..

rem Run the Python script with the provided model and scenarios
python ecosimp.py examples\ipd\config.json "%model%" "%scenarios%"

rem Navigate back to the ipd directory
cd examples\ipd

rem Render the R Markdown document to HTML
Rscript -e "rmarkdown::render('analisys/ipd.rmd', output_format='html_document', output_dir='results')"

rem Open the resulting HTML file in the default browser
start results\ipd.html

endlocal

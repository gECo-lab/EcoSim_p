class Result {

    constructor ()
    {

        this._btnSimulate = document.querySelector('.btn-simulate');

        this._aLinkZipCSV = document.querySelector('[link-download-zip-CSV]');

        this._aLinkDataVisualizaion = document.querySelector('[link-data-visualization]');

        this.initialize();

    }

    initialize () 
    {
       this.eventListeners();
    }

    // Events

    eventListeners ()
    {
        this._btnSimulate.addEventListener(["click"], event => {            

            let current_date = Date.now();

            let newHrefZipCSV = `/result/download/csv/${current_date}`;

            let newHrefDataVisualizaion = `/result/data-visualization/${current_date}`;

            this._aLinkZipCSV.setAttribute('href', newHrefZipCSV);

            this._aLinkDataVisualizaion.setAttribute('href', newHrefDataVisualizaion);            
            console.log('new href to result/download/csv and result/data-visualization');

        });     
    }
}

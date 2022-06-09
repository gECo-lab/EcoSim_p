class Header {

	constructor ()
	{
		this._navElementTitle = document.querySelector('nav-element-title');

		this.initialize();		
	}

	initialize ()
	{
		this.eventListeners();
	}

	// Events
	
	eventListeners ()
	{

		this._navElementTitle.addEventListener(["click"], event => {

			let url_github = "https://github.com/sergiolmrivero/EcoSim_p/tree/interface";

			window.open(url_github);

		});
	}
}

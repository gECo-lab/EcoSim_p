class Homepage {

	constructor(){

		this._formEl = document.querySelector("form");		

		this._arrayContent = Array.prototype.slice.call(document.querySelectorAll("content > [content]"));

		this._contentResultEl = document.querySelector("result");

		// Buttons

		this._btnModels = document.querySelector(".btn-models");
		this._btnSimulate = document.querySelector(".btn-simulate");		
		this._btnStop = document.querySelector(".btn-stop");
		this._btnResult = document.querySelector(".btn-result");

		this.initializate();
		
		this.onSubmit();

	}

	// Events

	addEventListenerToMenuItemToHideCorrespondingContent(contentSelectorEl, selector) {
		contentSelectorEl.addEventListener("click", e => {
			this.hideContent(selector);
		});		
	}

	addEventListenerToMenuItemToShowCorrespondingContent(contentSelectorEl, selector) {
		contentSelectorEl.addEventListener("click", e => {
			this.showContent(selector);			
		});		
	}

	showContent(selector)
	{

		this._arrayContent.forEach(contentEl => {

			// hiding displayed elements before show the clicked contentEl corresponding
			// to clicked menu item

			contentEl.style.display = "none";


		});

		document.querySelector(selector).style.display = "block";
	}

	hideContent(selector)
	{
		document.querySelector(selector).style.display = "none";
	}

	initializate()
	{

		document.querySelectorAll("sidebar > [content-selector]").forEach(contentSelectorEl => {

			const selector = contentSelectorEl.getAttribute("content-selector");

			this.addEventListenerToMenuItemToShowCorrespondingContent(contentSelectorEl, selector);

			});

		this._btnModels.addEventListener(["click"], event => {
			this._btnSimulate.style.display = 'block';
			caches.delete('result/download/csv');
		});

		this._btnResult.addEventListener(["click"], event => {
			this._btnSimulate.style.display = 'none';
		})
		
	}

	// APIs

    postResult(event)
    {
	    const form = event.target;

	    const data = new FormData(form);

	    data.append('ajax', true);

	    const options = {
	        method: form.method,
	        body: new URLSearchParams(data)
	    };
        
	    try
	    {   
	        // POST            
	        
	        fetch(form.action, options)
	            .then(resp => {	                

	                this.showContent("result");
	                
	                this._btnModels.style.display = "block";
	                this._btnSimulate.style.display = "none";	                
	                this._btnStop.style.display = "none";
	                this._btnResult.style.display = "block";	                

	            })

	    }

	    catch (e)
	    {
	        this._contentResultEl.innerHTML = e;
	    }

	}

	// Forms

	onSubmit()
	{
		this._formEl.addEventListener("submit", event => {

			event.preventDefault();			

			this.showContent("progress");
			
			this._btnModels.style.display = "none";
			this._btnSimulate.style.display = "none";			
			this._btnStop.style.display = "block";
			this._btnResult.style.display = "none";			
			
			this.showContent("progress");

			this.postResult(event);
			
		});
	}

}

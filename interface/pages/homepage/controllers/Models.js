class Models {

	constructor(){

		this._modelsEl = document.querySelector("models");

		this.initializate();			

	}


	initializate() {

		this.getModels();        

	}

    // APIs

    getModels(){
        const url = 'models';
            fetch(url)
                .then(resp => resp.json())
                .then(obj => {
                    let modelsEl = this.renderModels(obj.models);
                    this._modelsEl.appendChild(modelsEl);
                });

    }
    
    // Components
    
    renderModels = (models) => {
    	let modelsEl = document.createElement("div");

        function captilize(string){
            return string.replace(/^./, string[0].toUpperCase());
        }

        function split_names(string){
            return string.split("_").map(name => captilize(name)).join(" ");
        }    

    	modelsEl.innerHTML = `
            <h3>Models</h3>
    	 	<label for="select-model">Model: choose a model to simulate</label><br>
    		<select id="select-model" name="model">
				${
                    models.map(model => `<option value="${model}">${split_names(model)}</option>`).join("")
                }
    		</select>
    		<br><br>
    	`;
    	return modelsEl;
    }
	
}

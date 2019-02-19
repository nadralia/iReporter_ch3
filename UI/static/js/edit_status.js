if(!sessionStorage.token) {
	redirect:window.location.replace('./login.html');
}

//handling the map


const token = sessionStorage.token;
const incident_id = localStorage.recordId

// DECLARE VARIABLES
const status_field = document.getElementById('select_status');
//buttons
const btnEditStatus = document.getElementById('edit-status-btn');

//error and success 
let error = document.getElementById("error");
let success = document.getElementById("success");
{
	
	const url  = `${rootURL}/incidents/${incident_id}`;

	let options = {
        method: 'GET',
        headers: {
           'Content-type':'application/json',
            Authorization: `Bearer ${token}`
        }
    }

    let request = new Request(url, options);

    fetch(request)
	.then(response => response.json())
    .then(data => {
        console.log(data);
		var item_count = Object.keys("incident_details").length;
       
        if (item_count > 0){
            
			displayContents(data);
            
        }
        else{
            alert("here "+data.message)
        }
                
    })
    .catch(function (error) {
        console.log('Request failed', error);
    });
}

const displayContents = (data) => {
	// get values
	const spanIncidentId = document.getElementById('incident-id');
	const spanIncidentType = document.getElementById('incident-type');
	const spanStatus = document.getElementById('report-status');
	//set values
	spanIncidentId.textContent = data['incident_details']['incident_id']
	spanIncidentType.textContent = data['incident_details']['incident_type']
	spanStatus.textContent = data['incident_details']['status']
};

btnEditStatus.addEventListener('click', (ev) => {
    ev.preventDefault();    //stop the form submitting
	let incident_status = {
		status: status_field.value
	};
	const status_url  = `${rootURL}/incidents/${incident_id}/status`;
			
	let options = {
		method: 'PATCH',
		headers: {
			'Content-type':'application/json',
			Authorization: `Bearer ${token}`
				},
		mode: 'cors',
		body: JSON.stringify(incident_status)
	}
			
	let req = new Request(status_url,options);
	fetch(req)
		.then((response) => response.json())
		.then( (data)=>{
					
          console.log(data);
		   if (data.status === 400) {
                //validation error
                error.style.display = "block";
                error.innerHTML = data.message;

            } else if (data.status === 200) {
				success.style.display = "block";
				success.innerHTML = data["data"][0].message;
				setTimeout(()=> {
						redirect:window.location.reload(true);
						}, 1000);
				

            }else if(data.message ==="Signature has expired"){
				redirect:window.location.replace('./login.html');
			}
			else{
				throw new Error(data.error);
			}
		})
		.catch( (err) =>{
			console.log('ERROR:', err.message);
		});
	
});


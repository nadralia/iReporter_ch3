if(!sessionStorage.token) {
	redirect:window.location.replace('./login.html');
}

//handling the map


const token = sessionStorage.token;
const incident_id = localStorage.recordId

// DECLARE VARIABLES
const latitude = document.getElementById('latitude');
const longitude = document.getElementById('longitude');
const comment = document.getElementById('comment');
//buttons
const btnEditImages = document.getElementById('btn-edit-images');
const btnEditVideos = document.getElementById('btn-edit-videos');
const btnEditComment = document.getElementById('btn-edit-comment');
const btnEditLocation = document.getElementById('btn-edit-location');
const btnUpdateIncident = document.getElementById('edit-incident-btn');

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
	
	//set values
	spanIncidentId.textContent = data['incident_details']['incident_id']
	spanIncidentType.textContent = data['incident_details']['incident_type']
    comment.value = data['incident_details']['comment'];
	latitude.value = data['incident_details']['latitude'];
	longitude.value = data['incident_details']['longitude'];

};

const updateIncident =  () =>{
	const req = getRequestObj('updateIncident');
    fetch(req)
        .then(response => {
            return response.json();
        })
        .then(response => {
            if (response.status === 200) {

                // reload the page after 3 seconds
                setTimeout(() => {
                    window.location.reload(false);
                }, 2000);
            } else {
            }
        })
        .catch(err => {
         console.log(err);
        });
}

const patchComment = () => {
    let incident_comment = {
		comment: comment.value
	};
	const comment_url  = `${rootURL}/incidents/${incident_id}/comment`;
			
	let options = {
		method: 'PATCH',
		headers: {
			'Content-type':'application/json',
			Authorization: `Bearer ${token}`
				},
		mode: 'cors',
		body: JSON.stringify(incident_comment)
	}
			
	let req = new Request(comment_url,options);
	
    fetch(req)
        .then(response => {
            return response.json();
        })
        .then(data => {
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
        .catch(err => {
         console.log(err);
        });
};

const patchLocation = () => {
    let incident_status = {
		status: status_field.value
	};
	const status_url  = `${rootURL}/incidents/${incident_id}/location`;
			
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
    .then(response => {
        return response.json();
    })
    .then(response => {
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
    .catch(err => {
		console.log(err);
    });
};



btnUpdateIncident.addEventListener('click', (event) => {
    event.preventDefault();
    updateIncident();
});

btnEditComment.addEventListener('click', (event) => {
    event.preventDefault();
    patchComment();
});

btnEditLocation.addEventListener('click', (event) => {
    event.preventDefault();
	patchLocation

});



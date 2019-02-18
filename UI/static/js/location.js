if(!sessionStorage.token) {
	redirect:window.location.replace('./login.html');
}

const token = sessionStorage.token;
const incident_id = localStorage.incidentId

let latitude = document.getElementById('');
let longitude = document.getElementById('');
let loc_data ={
	latitude : latitude.value,
	longitude: longitude.value
}

function changeLocation(incident_id, loc_data) {
    const url = '';


    let options = {
        method: 'PATCH',
        body: JSON.stringify(loc_data),
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
		
    })
    .catch(function (error) {
        console.log('Request failed', error);
    });
}

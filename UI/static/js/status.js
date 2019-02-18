if(!sessionStorage.token) {
	redirect:window.location.replace('./login.html');
}

const token = sessionStorage.token;
const incident_id = localStorage.recordId

function changeStatus(incidentId) {
    const url = '';


    let options = {
        method: 'PATCH',
        body: JSON.stringify(data),
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

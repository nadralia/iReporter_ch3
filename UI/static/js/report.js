if(!sessionStorage.token) {
	redirect:window.location.replace('./login.html');
}

const token = sessionStorage.token;
const incident_id = localStorage.recordId

const report_id = document.getElementById('incident-id');
const report_type = document.getElementById('incident-type');
const location_body = document.getElementById('location');
const report_status = document.getElementById('report-status');
const comment_body = document.getElementById('comment-body');
const report_image = document.getElementById('report-image');
const report_video = document.getElementById('report-video');


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
        console.log(data['incident_details']);
		var item_count = Object.keys("incident_details").length;
       
        if (item_count > 0){
            
            // set values
			const latitude = data['incident_details']['latitude'];
			const longitude = data['incident_details']['longitude'];
			
			comment_body.textContent = data['incident_details']['comment'];
			report_id.textContent = data['incident_details']['incident_id'];
			report_type.textContent = data['incident_details']['incident_type'];
			
			location_body.textContent = `${latitude} ${longitude}`;
			report_status.textContent = data['incident_details']['status'];
        }
        else{
            alert("here "+data.message)
        }
                
    })
    .catch(function (error) {
        console.log('Request failed', error);
    });
}
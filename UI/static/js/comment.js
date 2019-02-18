if(!sessionStorage.token) {
	redirect:window.location.replace('./login.html');
}

const token = sessionStorage.token;
const incident_id = localStorage.incidentId
let editedComment = document.getElementById('comment');

function changeComment(incident_id, editedComment) {
    const url = '';


    let options = {
        method: 'PATCH',
        body: JSON.stringify(editedComment),
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

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


const getRequestObj = (str) => {
    const formdata = new FormData();
    const myHeaders = new Headers();
    const uri = `${rootURL}/incidents/${recordId}/${str}`;
    const images = imgFileInput.files;
    const videos = vidFileInput.files;

    myHeaders.append('x-auth-token', token);

    switch(str) {
        case('updateIncident'):
            formdata.append('location', coords.value);
            break;
		case('location'):
            formdata.append('location', coords.value);
            break;
        case('comment') : 
            formdata.append('comment', comment.value);
            break;
        case('editImage') :
            if (images.length > 0) {
                for (let i = 0; i < images.length; i += 1) {
                    formdata.append('images', images[i]);
                }
            }
            break;
        case('editVideo') : 
            if (videos.length > 0) {
                for (let i = 0; i < videos.length; i += 1) {
                    formdata.append('videos', videos[i]);
                }
            }
            break;
    }

    const options = {
        method: 'PATCH',
        mode: 'cors',
        headers: myHeaders,
        body: formdata,
    };

    const request = new Request(uri, options);

    return request;
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
    const req = getRequestObj('comment');
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
};

const patchLocation = () => {
    const req = getRequestObj('location');
    fetch(req)
    .then(response => {
        return response.json();
    })
    .then(response => {
        if (response.status === 200) {

            // reload the page after 3 seconds
            setTimeout(() => {
                window.location.reload(false);
            }, 3000);
        } else {
        }
    })
    .catch(err => {
		console.log(err);
    });
};

const changeImage = () => {
    const req = getRequestObj('editImage');
    fetch(req)
    .then(response => {
        return response.json();
    })
    .then(response => {
        if(response.status === 200) {
            setTimeout(() => {
                window.location.reload(false);
            }, 2000);
        } else {
        }
    })
    .catch(err => {
    });

};

const changeVideo = () => {
    const req = getRequestObj('editVideo');
    fetch(req)
    .then(response => {
        return response.json();
    })
    .then(response => {
        if(response.status === 200) {
            setTimeout(() => {
                window.location.reload(false); // reload the page after 2 seconds
            }, 2000);
        } else {
        }
    })
    .catch(err => {

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

btnEditImages.addEventListener('click', (event) => {
    event.preventDefault();

});

btnEditVideos.addEventListener('click', (event) => {
    event.preventDefault();

});


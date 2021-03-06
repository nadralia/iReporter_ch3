//fetch using a Request and a Headers objects
// uploading an image/video along with other POST data
//using jsonplaceholder for the data
if(!sessionStorage.token) {
	redirect:window.location.replace('./login.html');
}

const token = sessionStorage.token;

const url =`${rootURL}/incidents`;
const url2 = `${rootURL}/uploads`;  // endpoint where file will be uploaded

const incident_type = document.getElementById('incident_type');
const comment = document.getElementById('comment');
const latitude = document.getElementById('latitude');
const longitude = document.getElementById('longitude');
const image_file = document.getElementById('images');
const video_file = document.getElementById('videos');

const createIncidentBtn = document.getElementById('create-incident-btn');

image_file.addEventListener('change', () => {
    const files = image_file.files;
    const allowedImageTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif'];
    for (let i = 0; i < files.length; i += 1) {
        if (!allowedImageTypes.includes(files[i].type)) {
			error_message=""
            image_file.value = ""; // clear the content of the the file input element
            return;
        }
    }
});

video_file.addEventListener('change', () => {
    const files = video_file.files;
    const allowedImageTypes = ['video/mp4'];
    for (let i = 0; i < files.length; i += 1) {
        if (!allowedImageTypes.includes(files[i].type)) {
            video_file.value = ""; // clear the content of the the file input element
            return;
        } else if (files[i].size > 10000000) {
            videos.value = "";
            return;
        }
    }
});

image_file.addEventListener('change', function(event){
	var formData = new FormData();
	formData.append('file', image_file.files[0]);
	formData.append('upload_preset', cloudinary_upload_preset)
	
	axios({
		url: cloudary_URL,
		method: 'POST',
		headers:{
			'Content-Type':'application/x-www-form-urlencoded'
		},
		data:formData
	}).then(function(response){
		console.log(response);
		let images_file_url = response.data.secure_url; 
		createIncidentBtn.addEventListener('click', (ev) => {
			ev.preventDefault();    //stop the form submitting
			

			let formdata = new FormData();
			if(image_file.files.length > 0) {
					for (let i = 0; i < image_file.files.length; i++) {
						formdata.append('images', image_file.files[i]);
					}
				}
				if(video_file.files.length > 0) {
					for (let i = 0; i < video_file.files.length; i++) {
						formdata.append('videos', video_file.files[i]);
					}
				}
			
			let userData = {
				incident_type: incident_type.value,
				latitude: latitude.value,
				longitude: longitude.value,
				images: images_file_url,
				videos: video_file.files[0].name,
				comment: comment.value
			};

			
			let options = {
				method: 'POST',
				headers: {
				   'Content-type':'application/json',
					Authorization: `Bearer ${token}`
				},
				mode: 'cors',
				body: JSON.stringify(userData)
			}
			
			let req = new Request(url,options);
			fetch(req)
				.then((response) => response.json())
				.then( (data)=>{
					console.log(formdata);
					return fetch(url2, {
						method: 'POST',
						body: formdata
					});

				})
				.then(function(response){
				// do something with the response
					console.log(response.status);
					if (response.status === 200){
						setTimeout(()=> {
							
							redirect:window.location.replace('./view-reports.html');
						}, 3000);
					}
				
				})
				.catch( (err) =>{
					console.log('ERROR:', err.message);
				});
		});
		
	}).catch(function(err){
		console.log(err);
	});
	
});


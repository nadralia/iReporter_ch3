if(!sessionStorage.token) {
	redirect:window.location.replace('./login.html');
}

//get user details
const token = sessionStorage.token;
const user_firstname = sessionStorage.firstname || '';
const user_lastname = sessionStorage.lastname || '';
const user_username = sessionStorage.username || '';
const user_email = sessionStorage.email || '';
const user_gender = sessionStorage.gender || '';
const user_phonenumber = sessionStorage.phonenumber || '';
const profilePicture = sessionStorage.userPicture;

//get fields by ids
const email = document.getElementById('email');
const username = document.getElementById('username');
const fullname = document.getElementById('fullname');
const phonenumber = document.getElementById('phonenumber');
const gender = document.getElementById('gender');
const profile_pic = document.getElementById('profile-picture');
// The date atop the profile page
const date = document.getElementById('date');
date.innerHTML = (new Date()).toLocaleString();

//incident fields
const count_redflags = document.getElementById('count-redflags');
const drafted_redflags = document.getElementById('drafted-redflags');
const ui_redflags = document.getElementById('ui-redflags');
const resolved_redflags = document.getElementById('resolved-redflags');
const rejected_redflags = document.getElementById('rejected-redflags');

const count_interventions = document.getElementById('count-interventions');
const drafted_interventions = document.getElementById('drafted-interventions');
const ui_interventions = document.getElementById('ui-interventions');
const resolved_interventions = document.getElementById('resolved-interventions');
const rejected_interventions = document.getElementById('rejected-interventions');




const getUserProfileDetails = async () => {
    
    const options = { 
	    method: 'GET', 
		headers: {
			'Content-type':'application/json',
			Authorization: `Bearer ${token}`
                 } 
		};

    const redflags_url = "http://127.0.0.1:5000/api/v2/red-flags";
    const interventions_url = "http://127.0.0.1:5000/api/v2/interventions";
 
    try {
        const redflags_response = await fetch(redflags_url, options);
        const redflags = await redflags_response.json();
		  //console.log(redflags);
        const interventions_response = await fetch(interventions_url, options);
        const interventions = await interventions_response.json();
		//console.log(interventions);
        const incident_obj = {redflags: redflags.data, interventions: interventions.data};
        return incident_obj;
    } catch(err) {
       console.log('ERROR:', err);
    };
};
const arrayFilter = (status, arr) => {
    return arr.filter(element => element.status === status).length;
}; 

let profileDetails = async () => {
	const user_records = await getUserProfileDetails();
	
	const interventions_data = user_records.interventions;
    const redflags_data = user_records.redflags;
	
	//console.log(interventions_data);

    fullname.textContent = `${user_firstname} ${user_lastname}`;
    email.textContent = user_email;
	username.textContent = user_username
	//phonenumber.textContent = user_phonenumber
	//gender.textContent = user_gender
	if(redflags_data.length > 0){
		count_redflags.textContent = redflags_data.length;
		drafted_redflags.textContent = arrayFilter('drafted', redflags_data);
		rejected_redflags.textContent = arrayFilter('rejected', redflags_data);
		resolved_redflags.textContent = arrayFilter('resolved', redflags_data);
		ui_redflags.textContent = arrayFilter('under investigation', redflags_data);
		
	}else{
		message ="";
	}
	if (interventions_data.length > 0){
		count_interventions.textContent = interventions_data.length;
		drafted_interventions.textContent = arrayFilter('drafted', interventions_data);
		rejected_interventions.textContent = arrayFilter('rejected', interventions_data);
		resolved_interventions.textContent = arrayFilter('resolved', interventions_data);
		ui_interventions.textContent = arrayFilter('under investigation', interventions_data);
	}
    
	
};


window.addEventListener('load', () => {
    profileDetails();
});
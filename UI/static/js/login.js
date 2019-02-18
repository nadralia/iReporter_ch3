//get the login values from login forms
const username = document.getElementById('username');
const password = document.getElementById('password');
const url = "http://127.0.0.1:5000/api/v2/auth/login";
//get the login submit button
const loginBtn = document.getElementById('login-btn');

loginBtn.addEventListener('click', (event) => {
    event.preventDefault();
	
	let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');

     // user details 
     let loginData = {
        username: username.value,
        password: password.value
    };
    
    let options = {
        method: "POST",
        headers: headers,
        mode: "cors",
        body:JSON.stringify(loginData)
    }

    let request = new Request(url, options);
	
	fetch(request)
        .then((response) => response.json())
        .then((data) => {
            if (data.status === 400) {
                //validation error
                error.style.display = "block";
                error.innerHTML = data.message;

            } else if (data.status === 200) {
                //Logged in successfully and redirect to profile page
				sessionStorage.token = data["data"][0].token;
				sessionStorage.is_admin = data["data"][0]["user"].is_admin;
				sessionStorage.firstname = data["data"][0]["user"].firstname;
				sessionStorage.lastname = data["data"][0]["user"].lastname;
				sessionStorage.username = data["data"][0]["user"].username;
				sessionStorage.user_id = data["data"][0]["user"].user_id;
				sessionStorage.email = data["data"][0]["user"].email;
				sessionStorage.gender = data["data"][0]["user"].gender;
				sessionStorage.phonenumber = data["data"][0]["user"].phonenumber;
				//sessionStorage.profile_pic = data["data"][0]["user"].profile_pic;
				//console.log(data["data"][0]["user"].is_admin);
				if(data["data"][0]["user"].is_admin === "False") {
				    redirect:window.location.replace('./profile.html');
				} else {
				    redirect:window.location.replace('./admin.html');
				}

            }else{
				throw new Error(data.error);
			}
        })
        .catch( (err) =>{
            console.log('ERROR:', err);
        });
});
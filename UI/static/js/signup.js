//get the signup values from signup forms
const first_name = document.getElementById('firstname');
const last_name = document.getElementById('lastname');
const other_name = document.getElementById('othernames');
const email = document.getElementById('email');
const user_name = document.getElementById('username');
const password = document.getElementById('password');
const confirm_password = document.getElementById("confirmpassword");
const phone_number = document.getElementById('phonenumber');
const profile_picture = document.getElementById('profile-pic').files[0];
const gender = document.getElementById('gender');
const btnSignup = document.getElementById('btn-signup');

//error and success 
let error = document.getElementById("error");
let success = document.getElementById("success");

// check string length

function stringlength(inputtxt, minlength, maxlength)
{ 
    var field = inputtxt.value; 
    var mnlen = minlength;
    var mxlen = maxlength;

    if(field.length<mnlen || field.length> mxlen)
    { 
        let message
        message = "Between " +mnlen+ " and " +mxlen+ " characters"
        return message;
    }
    else
    { 
        return true;
    }
}

first_name.onkeyup = function () {
    let firstNameError = document.getElementById("firstname-error");

    correctLength = stringlength(first_name, 3, 20)
    if (correctLength== true){
        firstNameError.style.display = "none";
        first_name.setCustomValidity("");
    }else {
        firstNameError.style.display = "block";
        firstNameError.innerHTML = correctLength;
        first_name.setCustomValidity("Invalid firstname.");

    }

};

last_name.onkeyup = function () {
    let lastNameError = document.getElementById("lastname-error");

    correctLength = stringlength(last_name, 3, 20)
    if (correctLength== true){
        lastNameError.style.display = "none";
        last_name.setCustomValidity("");
    }else {
        lastNameError.style.display = "block";
        lastNameError.innerHTML = correctLength;
        last_name.setCustomValidity("Invalid lastname.");

    }

};

other_name.onkeyup = function () {
    let otherNameError = document.getElementById("othername-error");

    correctLength = stringlength(other_name, 3, 20)
    if (correctLength== true){
        otherNameError.style.display = "none";
        other_name.setCustomValidity("");
    }else {
        otherNameError.style.display = "block";
        otherNameError.innerHTML = correctLength;
        other_name.setCustomValidity("Invalid othername.");

    }

};

user_name.onkeyup = function () {
    let userNameError = document.getElementById("username-error");

    correctLength = stringlength(user_name, 8, 20)
    if (correctLength== true){
        userNameError.style.display = "none";
        user_name.setCustomValidity("");
    }else {
        userNameError.style.display = "block";
        userNameError.innerHTML = correctLength;
        user_name.setCustomValidity("Invalid username.");

    }

};

//check if its a valid email
function ValidateEmail()
{
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let emailError = document.getElementById("email-error");
    if(email.value.match(mailformat))
    {
        emailError.style.display = "none";
        email.setCustomValidity("");
    }
    else
    {
        emailError.style.display = "block";
        emailError.innerHTML = "You have entered an invalid email address!";
        email.setCustomValidity("Invalid Email.");
    }
}

email.onblur = ValidateEmail;

function checkIfPasswordMatch() {
    let passwordError = document.getElementById("pass-error");
    if (password.value == confirm_password.value) {
        passwordError.style.display = "none";
    } else {
        
        passwordError.style.display = "block";
        passwordError.innerHTML = "Passwords doesn't  match";
    }

}

confirm_password.onblur = checkIfPasswordMatch;
confirm_password.onkeyup = checkIfPasswordMatch;


//check if its a valid phonenumber
function phoneNumber()
{
  var phoneno = /^\d{10}$/;
  let phoneError = document.getElementById("phone-error");
  if(phone_number.value.match(phoneno))
  {
    phoneError.style.display = "none";
    phone_number.setCustomValidity("");

  }
  else
  {
    phoneError.style.display = "block";
    phoneError.innerHTML = "Not a valid Phone Number";
    phone_number.setCustomValidity("Wrong Phonenumber Format.");
  }
}

phone_number.onkeyup = phoneNumber;


btnSignup.addEventListener('click', (event) => {
    event.preventDefault();//stop the form submitting
	
	//create any headers we want
	let header = new Headers();
    header.append('Content-Type', 'application/json');
    header.append('Accept', 'application/json');
	
	// file that has been selected in the form
	const input = document.querySelector('input[type="file"]');
	
	let formdata = new FormData();
    formdata.append('file', input.files[0]);

	// user details 
    let userData = {
        firstname: first_name.value,
        lastname: last_name.value,
        othernames: other_name.value,
        email: email.value,
        password: password.value,
        username: user_name.value,
        phonenumber: phone_number.value,
        gender: gender.value,
		is_admin:"False"
    };
	const url = `${rootURL}/auth/signup`;
	const url2 = `${rootURL}/profilepic`;  // endpoint where file will be uploaded
    const options = { method: 'POST',headers: header, mode: 'cors', body:JSON.stringify(userData) };
    const request = new Request(url, options);
	
	fetch(request)
        .then((response) => response.json())
        .then((data) => {
            if (data.status === 400) {
                //validation error
                error.style.display = "block";
                error.innerHTML = data.message;
            } else if (data.status === 409) {
                //user exists error
                error.style.display = "block";
                error.innerHTML = data.message;

            } else if (data.status === 201) {
                //User account created and redirect to login page
				success.style.display = "block";
                success.innerHTML = data["data"][0].message;
				return fetch(url2, {
				method: 'POST',
				body: formdata
			    });
                
            }else {
                // throw new Error
                error.style.display = "block";
                error.innerHTML = data;
            }
        }).then(function(response){
        // do something with the response
			setTimeout(()=> {
                    redirect:window.location.replace('./login.html');
                }, 3000);
        })
        .catch( (err) =>{
            console.log('ERROR:', err);
        });
	
});
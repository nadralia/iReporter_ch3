const rootURL = 'http://127.0.0.1:5000/api/v2';

//sign-out link
signOut = document.querySelectorAll('.sign-out');


// The 'sign-out' operation can be performed thus:
signOut.forEach(link => {
    link.addEventListener('click', () => {
        sessionStorage.removeItem('token');
        sessionStorage.removeItem('firstname');
        sessionStorage.removeItem('lastname');
        sessionStorage.removeItem('username');
        sessionStorage.removeItem('user_id');
        sessionStorage.removeItem('email');
		sessionStorage.removeItem('gender');
		sessionStorage.removeItem('phonenumber');
    });
});

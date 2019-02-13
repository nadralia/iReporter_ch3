const rootURL = 'https://dbireporter.herokuapp.com/api/v2';

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

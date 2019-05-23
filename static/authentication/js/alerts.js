
document.querySelector("#register-user").addEventListener('click', function(){
    Swal.fire({
        title: 'This is a beta version. Contact with the administrator to get access.',
        width: 600,
        padding: '3em',
        background: '#fff url('+trees+')',
        backdrop: 'rgba(0,0,123,0.4) url('+nyanCat+') center left no-repeat'
    })
});


document.querySelector("#forgot-pass").addEventListener('click', function(){
    Swal.fire({
        type: 'question',
        title: 'Forgot your password?',
        text: 'Contact with the administrator who gave you the credentials to get a new ones.'
    })
});
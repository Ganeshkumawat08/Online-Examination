// function login() {
//     let userid = document.getElementById('userid').value;
//     let password = document.getElementById('password').value;
//     if (!userid && !password) {
//         alert("Enter userid or password");
//         return;
//     }
//     else {
//         window.location.href = '/examapp/login';
//     }
// }


function conform(button) {
    c = confirm('delete')
    if (c) {
        window.location.href = `/examapp/delete/${button.value}/${button.id}`;
    }
    else {
        return;
    }
}



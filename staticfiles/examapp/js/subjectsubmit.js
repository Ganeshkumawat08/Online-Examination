let subject = localStorage.getItem('subject');
let mark = localStorage.getItem(subject);
let totalque = localStorage.getItem('totalque');


percentage=(mark/totalque)*100
if(percentage>33){
    result="PASS";
 }else{
     result="FAIL";
 }

document.getElementById('subject').value = subject
document.getElementById('marks').value = mark
document.getElementById('questions').value = totalque
document.getElementById('percentage').value = percentage
document.getElementById('result').value = result

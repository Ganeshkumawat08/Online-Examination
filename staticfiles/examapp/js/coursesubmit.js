let course = localStorage.getItem('course')
let subjects = JSON.parse(localStorage.getItem('subjects'));
let totalque = JSON.parse(localStorage.getItem('totalque'));

let sub = []
let mark = 0
let totalmarks = 0
let questions=0
let result=""


for (let x = 0; x < totalque.length; x++) {
    questions+=totalque[x]
}

for (s in subjects) {
    sub.push(subjects[s])
    mark = localStorage.getItem(subjects[s]);
    sub.push(mark);
    totalmarks = totalmarks + parseInt(mark);
}

percentage=(totalmarks/questions)*100
if(percentage>33){
    result="PASS";
 }else{
     result="FAIL";
 }

document.getElementById('course').value = course
document.getElementById('subjects').value = sub
document.getElementById('totalmarks').value = totalmarks
document.getElementById('questions').value = questions
document.getElementById('percentage').value = percentage
document.getElementById('result').value = result


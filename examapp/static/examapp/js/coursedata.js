localStorage.clear()
localStorage.setItem('method', 'course')

userid = document.getElementById('user').innerText;
localStorage.setItem('userid', userid)

let course = document.getElementById('course').innerText;
localStorage.setItem('course', course)

let listItems = document.querySelectorAll("#subjectList li");
let subjects = [];
listItems.forEach(item => {
    subjects.push(item.textContent);
});
localStorage.setItem("subjects", JSON.stringify(subjects));
localStorage.setItem('totalsubject', subjects.length)


listItems = document.querySelectorAll("#totalque li");
totalque = [];
listItems.forEach(item => {
    totalque.push(parseInt(item.textContent));
});

localStorage.setItem("totalque", JSON.stringify(totalque));

localStorage.setItem("sub", '0');
localStorage.setItem("que", '0');



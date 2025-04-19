function startexam() {
    let sub = parseInt(localStorage.getItem('sub'));
    let que = parseInt(localStorage.getItem('que'));
    let totalsub = parseInt(localStorage.getItem('totalsubject'));
    let subjects = JSON.parse(localStorage.getItem('subjects'));
    let totalque = JSON.parse(localStorage.getItem('totalque'));
    if (sub < totalsub) {
        if (que < totalque[sub]) {
            window.location.href = `/examapp/question/${subjects[sub]}/${que}`
        } else {
            alert('Does not set Question!');
            return;
        }
    }
    else {
        alert('Does not set subject!');
        return;
    }
}


function submitcourseque() {
    let sub = parseInt(localStorage.getItem('sub')) || 0;
    let que = parseInt(localStorage.getItem('que')) || 0;
    let totalsub = parseInt(localStorage.getItem('totalsubject')) || 0;
    let totalque = JSON.parse(localStorage.getItem('totalque')) || [];
    let subjects = JSON.parse(localStorage.getItem('subjects')) || [];
    let id = parseInt(document.getElementById("id").innerText) || 0;

    let selectedOption = document.querySelector('input[name="option"]:checked');
    let answer = parseInt(document.getElementById('answer').value) || 0;

    if (!selectedOption) {
        alert("Please select an option!");
        return;
    }

    let selected_value = parseInt(selectedOption.value);
    let marks = (answer === selected_value) ? 1 : 0;

    const data = [que, id, selected_value, marks];
    localStorage.setItem(que, JSON.stringify(data));

    if (sub < totalsub) {
        que++;
        if (que < totalque[sub]) {
            localStorage.setItem("que", que);
            id++;
            window.location.href = `/examapp/question/${subjects[sub]}/${id}`;
        } else {
            let correct = 0;
            for (let x = 0; x <= que; x++) {
                let storedData = JSON.parse(localStorage.getItem(x));
                if (storedData) {
                    correct += storedData[3];
                }
            }
            localStorage.setItem(subjects[sub], correct);
            sub++;
            localStorage.setItem("sub", sub);
            localStorage.setItem("que", '0');

            if (sub < totalsub) {
                window.location.href = `/examapp/question/${subjects[sub]}/0`;
            } else if (confirm('Submit paper?')) {
                let userid = localStorage.getItem('userid');
                window.location.href = `/examapp/resultcourse/${userid}`;
            }
        }
    } else if (confirm('Submit paper?')) {
        userid = localStorage.getItem('userid');
        window.location.href = `/examapp/resultcourse/${userid}`;
    }
}


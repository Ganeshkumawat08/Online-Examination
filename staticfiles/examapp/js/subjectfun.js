function startexam() {
    let que = parseInt(localStorage.getItem('que'));
    let subject = localStorage.getItem('subject');
    let totalque = localStorage.getItem('totalque');
    if (que < totalque) {
        window.location.href = `/examapp/question/${subject}/${que}`
    } else {
        alert('Does not set Question!')
        return
    }
}


function submitsubjectque() {
    let que = parseInt(localStorage.getItem('que')) || 0;
    let totalque = localStorage.getItem('totalque') || [];
    let subject = localStorage.getItem('subject') || [];
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

    que++;
    if (que < totalque) {
        localStorage.setItem("que", que);
        id++;
        window.location.href = `/examapp/question/${subject}/${id}`;
    } else {
        let correct = 0;
        for (let x = 0; x <= que; x++) {
            let storedData = JSON.parse(localStorage.getItem(x));
            if (storedData) {
                correct += storedData[3];
            }
        }
        localStorage.setItem(subject, correct);
        if (confirm('Submit paper?')) {
            let userid = localStorage.getItem('userid');
            window.location.href = `/examapp/resultsubject/${userid}`;
        }
    }
}


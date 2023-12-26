document.getElementById('addApplication').addEventListener('click', function() {
    var form = document.getElementById('addAppli');
    form.style.display = 'block';

    document.getElementById('addApplication').style.display = 'none';
    document.getElementById('HiddenApplication').style.display = 'block';
});

document.getElementById('HiddenApplication').addEventListener('click', function() {
    var form = document.getElementById('addAppli');
    form.style.display = 'none';

    document.getElementById('HiddenApplication').style.display = 'none';
    document.getElementById('addApplication').style.display = 'inline';
});



document.getElementById('addAppli').addEventListener('submit', function(event) {
    event.preventDefault();

    var courseData = {
        name: event.target.name.value,
        numberOfPeople: event.target.numberOfPeople.value,
        whereFrom: event.target.WhereFrom.value,
        whereTo: event.target.WhereTo.value,
        data: event.target.Data.value,
        time: event.target.Time.value,
        phoneNumber: event.target.phoneNumber.value,
        money: event.target.Money.value,
    };

    fetch('/new_application', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: courseData
    })
    .then(response => {
        if (response.status === 200) {
            ws.send(JSON.stringify(courseData))
            return response.json();
        } else {
            throw new Error('Ошибка сервера: ' + response.status);
        }
    })
    .catch(error => console.error('Ошибка при отправке данных:', error));
    event.target.reset();
});
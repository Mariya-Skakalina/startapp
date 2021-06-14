let elem = document.querySelector('#date_of_birth')
let save_date = document.querySelector('#save_date')

elem.addEventListener('click', () => {
    save_date.style.display = 'block'
})

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

save_date.onclick = async (e) => {
    e.preventDefault();

    let response = await fetch(document.location.origin + '/api/date/',{
        method: 'POST',
        credentials: 'same-origin',
        body: JSON.stringify({
            'age': document.getElementById('date_of_birth').value,
        }),
        headers: {
            'Content-Type':'application/json',
            // 'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRFToken':csrftoken,
        }
    });

    let result = await response.json();

    alert("Ok");
};

// save_date.addEventListener('click', () => {
//     fetch(document.location.origin + '/api/date/',{
//         method: 'post',
//         credentials: 'same-origin',
//         body: new FormData(document.getElementById('date_post')),
//         headers:MyHeaders
//     }).then(function (res) {
//         console.log(res)
//         return res.json()
//     })
//     .catch(error => console.log(error));
// })

let elem = document.querySelector('#date_of_birth')
let save_date = document.querySelector('#save_date')

elem.addEventListener('click', () => {
    save_date.style.display = 'block'
})

let MyHeaders = new Headers();
MyHeaders.append('Accept', 'application/json');

save_date.addEventListener('click', () => {
    fetch(document.location.origin + '/api/date/',{
        method: 'post',
        data: new FormData(document.getElementById('date_post')),
        headers:MyHeaders
    }).then(function (res) {
        return res.json()
    })
})

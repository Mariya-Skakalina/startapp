document.querySelector('#profile_user').addEventListener('click', ()=>{
    let profile = document.querySelector('#profile')
    let pr_style = getComputedStyle(profile)
    if (getComputedStyle(profile).display == 'none') {
        profile.style.display = 'block'
    } else {
        profile.style.display = 'none'
    }
})


















let elem = document.querySelector('#date_of_birth')
let save_date = document.querySelector('#save_date')

if (elem) {
    elem.addEventListener('click', () => {
        save_date.style.display = 'block'
    })
}

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

if (save_date) {
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
            'Accept': 'application/json',
            'X-CSRFToken':csrftoken,
        }
    });

    let result = await response.json();
};
}

let save_skills = document.querySelector('#save_skills')

save_skills.addEventListener('click', ()=>{
    fetch(document.location.origin + '/api/skill_add/',{
        method: 'post',
        credentials: 'same-origin',
        body: JSON.stringify({
            'name': document.getElementById('skill_name').value,
        }),
        headers: {
            'Content-Type':'application/json',
            'Accept': 'application/json',
            'X-CSRFToken':csrftoken,
        }
    }).then(function (res) {
        console.log(res)
        return res.json()
    })
    .catch(error => console.log(error));
})

fetch(document.location.origin + '/api/skills/', {
    method: 'get',
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
})
.then((resp) => resp.json())
.then(function(data) {
    console.log(data)
    for (let prop of data) {

        let p = document.createElement('p')
        p.className = "skill"
        p.innerText = prop.name
        p.id = prop.id
        document.getElementById('skills_all').prepend(p)
  console.log(prop['name']);
    }
})
.catch(function(error) {
  console.log(error);
});

let div = document.querySelector('#skills_all')

div.addEventListener('click', function (event){
    let skill = event.target
    fetch(document.location.origin + '/api/delete_skill/'+skill.id,{
        method: 'delete',
        credentials: 'same-origin',
        // body: JSON.stringify({
        //     'pk': skill.id,
        // }),
        headers: {
            'Content-Type':'application/json',
            'Accept': 'application/json',
            'X-CSRFToken':csrftoken,
        }
    }).then(function (res) {
        console.log('ok')
        return res.json()
    })
    .catch(error =>console.log(error));
})
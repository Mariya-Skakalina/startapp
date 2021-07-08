let profile_user = document.querySelector('#profile_user')
if (profile_user) {
    profile_user.addEventListener('click', ()=>{
    let profile = document.querySelector('#profile')
    let pr_style = getComputedStyle(profile)
    if (getComputedStyle(profile).display == 'none') {
        profile.style.display = 'block'
    } else {
        profile.style.display = 'none'
    }
})
}



let elem = document.querySelector('#date_of_birth')
let save_date = document.querySelector('#save_date')

if (elem) {
    elem.addEventListener('click', () => {
        save_date.style.display = 'block'
    })
}

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

//Добавление даты рождения
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

//Добавление навыка
if(save_skills) {
    save_skills.addEventListener('click', ()=>{
    fetch(document.location.origin + '/api/skill_add/',{
        method: 'post',
        credentials: 'same-origin',
        body: JSON.stringify({
            'id_project': Number(document.querySelector('#skill_name').getAttribute('id_project')),
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
}


let skill_all = document.querySelector('#skills_all')

// вывод добавленных навыков пользователя
if (skill_all) {
    fetch(document.location.origin + '/api/skills/' + skill_all.getAttribute('id_prc'), {
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
}

//удаление навыка
let div = document.querySelector('#skills_all')
if(div) {
    div.addEventListener('click', function (event){
    let skill = event.target
    fetch(document.location.origin + '/api/delete_skill/'+skill.id + '/' + div.getAttribute('id_prc'),{
        method: 'delete',
        credentials: 'same-origin',
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
}




// Добавление тэгов
let save_tag = document.querySelector('#save_tag')
if (save_tag) {
    save_tag.addEventListener('click', ()=>{
    fetch(document.location.origin + '/api/tag_add/',{
        method: 'post',
        credentials: 'same-origin',
        body: JSON.stringify({
            'id_project': document.querySelector('#tag_name').getAttribute('id_project'),
            'name': document.querySelector('#tag_name').value,
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
}

//Вывод тэгов проекта
fetch(document.location.origin + '/api/tags/'+document.querySelector('#tag_all').getAttribute('id_prc'), {
    method: 'get',
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
})
.then((resp) => resp.json())
.then(function(data) {
    for (let prop of data) {

        let p = document.createElement('p')
        p.className = "tag"
        p.innerText = prop.name
        p.id = prop.id
        document.getElementById('tag_all').prepend(p)
    }
})
.catch(function(error) {
  console.log(error);
});

//удаление Тэга
let div1 = document.querySelector('#tag_all')
if(div1) {
    div1.addEventListener('click', function (event){
    let tag = event.target
    fetch(document.location.origin + '/api/delete_tag/'+tag.id + '/' + document.querySelector('#tag_all').getAttribute('id_prc'),{
        method: 'delete',
        credentials: 'same-origin',
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
}


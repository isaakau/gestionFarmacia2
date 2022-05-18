var updateBtns = document.getElementsByClassName('update-receta')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var medId = this.dataset.med
        var action = this.dataset.action
        console.log('id:',medId, 'action:',action, 'test' )
        updateUserReceta(medId,action)
    })
}

function updateUserReceta(medId,action){
    console.log('++++++++++++')

    var url = '/updateMed/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'medId':medId,'action':action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:',data)
    })
}

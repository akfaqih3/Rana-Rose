function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


const inputs = document.querySelectorAll('input,textarea,select');

for (const input of inputs){
    if (input.nodeName === 'TEXTAREA'){
        input.style.height = '4em';
        input.style.resize = 'none';
    }
    input.classList.add('form-control');
};

const cart_btns = document.getElementsByClassName('btn_product');

for (const btn of cart_btns){
    btn.addEventListener('click',function(e){
        if (e.target.id == "add") {
            addToCart(e.target);
        }else{
            removeFromCart(e.target);
        }
        e.target.classList.toggle('btn-success')
        e.target.classList.toggle('btn-outline-danger')
        //e.target.childNode('i')[0].classList.toggle('fa-trash')
    });
};

function addToCart(target){
    const data = {pk:Number(target.dataset.product)}
    let url = `Cart/addToCart/`

    fetch(
        url,{
            method:'POST',
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken
            },
            body: JSON.stringify(data)
        }
    )
    .then(
        (response)=>{
            if(!response.ok){
                throw new Error(`HTTP error :${response.Error}`)
            }
            return response.json()
        }
    )
    .then(
        (data)=>{
            showResult(data);
            target.id = "delete";
        }
    ).catch(
        (error)=>{
            if (error == 'SyntaxError: Unexpected token \'<\', "<!DOCTYPE "... is not valid JSON'){
                window.location.pathname = "/Account/login/"
            }
        }
    )
}

function removeFromCart(target){
    const data = {pk:Number(target.dataset.product)}
    let url = `Cart/removeFromCart/`

    fetch(
        url,{
            method:'POST',
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken
            },
            body: JSON.stringify(data)
        }
    )
    .then(
        (response)=>{
            if(!response.ok){
                throw new Error(`HTTP error :${response.Error}`)
            }
            return response.json()
        }
    )
    .then(
        (data)=>{
            showResult(data);
            target.id = "add";
        }
    )
    .catch(
        (error)=>{
            if (error == 'SyntaxError: Unexpected token \'<\', "<!DOCTYPE "... is not valid JSON'){
                window.location.pathname = "/Account/login/"
            }
        }
    )
}

function showResult(data){
    cart_badge = document.getElementById('cart_badge')
    cart_badge.innerText = data.length
    
    for (const btn of cart_btns){
        if (data.pks.includes(Number(btn.dataset.product))){
            btn.id = "delete";
            btn.classList.replace('btn-success','btn-outline-danger');
        }else{
           btn.id = "add";
           btn.classList.replace('btn-outline-danger','btn-success')
        }
    };
}
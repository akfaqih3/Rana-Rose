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
    var cart = data
    cart_badge = document.getElementById('cart_badge');
    cart_badge.innerText = cart.products.length;
    updateCart(cart);
    for (const btn of cart_btns){
        if (cart.pks.includes(Number(btn.dataset.product))){
            btn.id = "delete";
            btn.classList.replace('btn-success','btn-outline-danger');
            btn.classList.replace('fa-cart-plus','fa-trash');
        }else{
           btn.id = "add";
           btn.classList.replace('btn-outline-danger','btn-success')
           btn.classList.replace('fa-trash','fa-cart-plus')
        }
    };
}

function updateCart(cart){
    cart_count = document.getElementById('cart_count');
    cart_total = document.getElementById('cart_total');
    cart_body = document.getElementById('cart_body');
    cart_count.innerText=`Products Count: ${cart.products.length}`;
    cart_total.innerText = cart.cart_total;

    cart_body.innerHTML = ''
    cart.products.forEach(product => {
        new_row = `<tr>
        <td><img src ='${product.photo}' width="40" height="36"></td>
        <td><h6 class="fw-normal">${product.name}</h6></td>
        <td><h6 class="fw-normal">${product.price}</h6></td>
        </tr>`
        cart_body.innerHTML +=new_row;
    });
}
const inputs = document.querySelectorAll('input,textarea,select');

for (const input of inputs){
    if (input.nodeName === 'TEXTAREA'){
        input.style.height = '4em'
        input.style.resize = 'none'
    }
    input.classList.add('form-control')
}

const products = document.getElementById('products');

products.addEventListener('click',function(event){
        if (event.target.tagName == 'BUTTON'){
            const btn = event.target
            const icon = btn.firstElementChild
            btn.classList.toggle('btn-outline-danger')
            btn.classList.toggle('btn-success')
            icon.classList.toggle('fa-trash')
            

            cart_badge = document.getElementById('cart_icon').querySelector('span')
            if (icon.classList.contains('fa-trash')){
                cart_badge.innerText = Number(cart_badge.innerText)+1;
            }else{
                cart_badge.innerText = Number(cart_badge.innerText)-1;
            }

        }
        
    })
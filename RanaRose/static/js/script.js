const inputs = document.querySelectorAll('input,textarea,select');

for (const input of inputs){
    if (input.nodeName === 'TEXTAREA'){
        input.style.height = '4em'
        input.style.resize = 'none'
    }
    input.classList.add('form-control')
}

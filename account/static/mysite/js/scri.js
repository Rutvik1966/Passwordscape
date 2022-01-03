console.log("H");
const btns=[...document.getElementsByClassName('copybtn')]
console.log(btns);
btns.forEach(btn=>btn.addEventListener('click',()=>{
    const password=btn.getAttribute('pass')
    navigator.clipboard.writeText(password)
    btn.textContent="Copied"
}))
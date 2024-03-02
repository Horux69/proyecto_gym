const openModal2 = document.querySelector('.boton_ope2');
const modal2 = document.querySelector('.modal2');
const modalClose2 = document.querySelector('.modal_close2');

openModal2.addEventListener('click', (e)=>{
    e.preventDefault();
    modal2.classList.add('modal--show');
});

modalClose2.addEventListener('click', (e)=>{
    e.preventDefault();
    modal2.classList.remove('modal--show');
});

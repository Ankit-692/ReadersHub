const cards = document.querySelectorAll('.bookCard')
const blurr = document.querySelector('.blur')

cards.forEach(card=>{
    card.querySelector('.image-banner').addEventListener('click',()=>{
        blurr.classList.remove('hide')
        card.querySelector('.card').querySelector('.grid').querySelector('.description').classList.remove('hide')
    blurr.addEventListener('click',()=>{
            card.querySelector('.card').querySelector('.grid').querySelector('.description').classList.add('hide')
            blurr.classList.add('hide')

        })
    })
})


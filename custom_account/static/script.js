
console.log(window.scrollY+window.innerHeight)
const header = document.querySelector('header');
const targetUserNames = document.getElementsByClassName('target-user');
const selectedTargetUsersList = document.querySelector('#selected-target-users')

// search form
let username = ''
const searchForm = document.querySelector('.search-form');
// search input
const searchUsername = document.querySelector('#search-username');
searchUsername.addEventListener('change', ()=>{username = searchUsername.value})

searchForm.addEventListener('submit', (e)=>{
    e.preventDefault = false;
    console.log(username)
    searchUsername.value = username;

})

console.log(targetUserNames)

for(let index = 0; index < targetUserNames.length; index++){
    targetUserNames[index].addEventListener('click', ()=>{
    const label  = document.querySelector(`#label-${index}`).innerHTML;
    const checkbox = document.querySelector(`#checkbox-${index}`)
    if(checkbox.checked === true){
        child = document.querySelector(`#target-user-item-${index}`)
        selectedTargetUsersList.removeChild(child)
        checkbox.checked = false
    }else{
        checkbox.checked = true
        selectedTargetUsersList.appendChild(createTargetUserItem(label, index))
    }
})
}

function createTargetUserItem(label, index){
    const li = document.createElement('li')
    li.id = `target-user-item-${index}`
    li.className = 'selected-target-user'
    li.innerHTML = label;
    return li
}

window.onscroll = (e)=>{
    if(window.scrollY > 0){
        header.style.backgroundColor = 'white';
    }else{
        header.style.backgroundColor = '#dcdcdc';
        header.style.boxShadow = '0px 1px 2px gray'
    }
}

const barsIcon = document.querySelector('header .fa-bars');
const navBar = document.querySelector('header nav');
// Display modal when nav-bar icon is clicked
let clicked = false;
barsIcon.onclick = ()=>{
    if (clicked){
        navBar.setAttribute('class', 'hide-nav-modal');
        clicked = false;
        console.log('hide')
    }else{
        navBar.setAttribute('class', 'show-nav-modal');
        clicked = true;
        console.log('show')
    }
    
}
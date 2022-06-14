const targetUserNames = document.getElementsByClassName('target-user');
const selectedTargetUsersList = document.querySelector('#selected-target-users')

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
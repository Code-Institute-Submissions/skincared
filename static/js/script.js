const userProfileIcon = document.getElementById('profile-icon');
const userProfileDropDown = document.querySelector('.user-profile-drop-down-menu'); 


console.log(userProfileIcon)
console.log(userProfileDropDown)

userProfileIcon.addEventListener("click", function(){
    userProfileDropDown.classList.toggle("profile-active"); 
})


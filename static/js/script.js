// User Profile Dropdown Toggle 
const userProfileIcon = document.getElementById('profile-icon');
const userProfileDropDown = document.querySelector('.user-profile-drop-down-menu'); 

userProfileIcon.addEventListener("click", function(){
    userProfileDropDown.classList.toggle("profile-active"); 
})


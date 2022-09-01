// User Profile Dropdown Toggle 
const userProfileIcon = document.getElementById('profile-icon');
const userProfileDropDown = document.querySelector('.user-profile-drop-down-menu'); 

userProfileIcon.addEventListener("click", function(){
    userProfileDropDown.classList.toggle("profile-active"); 
})

const navHeading = document.querySelectorAll('.nav-heading'); 
const navDropDown = document.querySelectorAll('.nav-drop-down'); 

console.log(navHeading)
console.log(navDropDown)

navHeading[0].addEventListener("click", function(){
    navDropDown[0].classList.toggle("nav-active");
} )
// navHeading.forEach(function)
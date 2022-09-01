// Main Header User Profile Dropdown 
const userProfileIcon = document.getElementById('profile-icon');
const userProfileDropDown = document.querySelector('.user-profile-drop-down-menu'); 

userProfileIcon.addEventListener("click", function(){
    userProfileDropDown.classList.toggle("profile-active"); 
})

// Mobile Header Dropdowns 
const hamburger = document.querySelector(".burger-menu"); 
const navMenu = document.querySelector(".test"); 

console.log(hamburger)

console.log(navMenu)

hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("active");  
})

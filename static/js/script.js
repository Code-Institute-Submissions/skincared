// Main Header & Mobile Header  User Profile Dropdown 
const userProfileIcon = document.querySelectorAll('.profile-icon');
const userProfileDropDown = document.querySelectorAll('.user-profile-drop-down-menu'); 

for (let i = 0; i < userProfileIcon.length; i++) {
    userProfileIcon[i].addEventListener("click", function() {
        for (let i = 0; i < userProfileDropDown.length; i++) {
            userProfileDropDown[i].classList.toggle("profile-active");    
        }
    })
}

// Mobile Navigation Dropdown 
const hamburger = document.querySelector(".burger-menu"); 
const navMenu = document.querySelector(".main-navigation"); 

hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("nav-active");
})

// Mobile Serach Bar Dropdown 
const searchIcon = document.querySelector(".search-bar-mobile"); 
const search = document.querySelector(".mobile-serach-bar-container");

searchIcon.addEventListener("click", () =>{
    search.classList.toggle("active");
})
// Main Header User Profile Dropdown 
const userProfileIcon = document.querySelector('.profile-icon');
const userProfileDropDown = document.querySelector('.user-profile-drop-down-menu'); 

userProfileIcon.addEventListener("click", function(){
    userProfileDropDown.classList.toggle("profile-active"); 
})

// Mobile Navigation Dropdown 
const hamburger = document.querySelector(".burger-menu"); 
const navMenu = document.querySelector(".mobile-nav-bar"); 

hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("active");  
})

// Mobile Serach Bar Dropdown 
const searchIcon = document.querySelector(".search-bar-mobile"); 
const search = document.querySelector(".mobile-serach-bar-container");

console.log(searchIcon)
console.log(search)

searchIcon.addEventListener("click", () =>{
    search.classList.toggle("active");
})
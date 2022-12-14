// User Profile Dropdown 
const userProfileIcon = document.querySelectorAll('.profile-icon');
const userProfileDropDown = document.querySelectorAll('.user-profile-drop-down-menu'); 

for (let i = 0; i < userProfileIcon.length; i++) {
    userProfileIcon[i].addEventListener("click", function() {
        for (let i = 0; i < userProfileDropDown.length; i++) {
            userProfileDropDown[i].classList.toggle("profile-active");    
        }
    })
}

// Main Navigation 
const navButtonSkin = document.querySelector(".js-nav-button-skincare");
const navDropDownSkin = document.querySelector(".skincare-container")

navButtonSkin.addEventListener("mouseenter", () => {
    navDropDownSkin.classList.add("main-nav-js")
})

navDropDownSkin.addEventListener("mouseleave", () => {
    navDropDownSkin.classList.remove("main-nav-js")
})

const navButtonBrand = document.querySelector(".js-nav-button-brands");
const navDropDownBrand = document.querySelector(".brands-container")

navButtonBrand.addEventListener("mouseenter", () => {
    navDropDownBrand.classList.add("main-nav-js")
})

navDropDownBrand.addEventListener("mouseleave", () => {
    navDropDownBrand.classList.remove("main-nav-js")
})

const navButtonSkinType = document.querySelector(".js-nav-button-skin-type");
const navDropDownSkinType = document.querySelector(".skin-type-container")

navButtonSkinType.addEventListener("mouseenter", () => {
    navDropDownSkinType.classList.add("main-nav-js")
})

navDropDownSkinType.addEventListener("mouseleave", () => {
    navDropDownSkinType.classList.remove("main-nav-js")
})

const navButtonSkinConcern = document.querySelector(".js-nav-button-skin-concern");
const navDropDownSkinConcern = document.querySelector(".skin-concern-container")

navButtonSkinConcern.addEventListener("mouseenter", () => {
    navDropDownSkinConcern.classList.add("main-nav-js")
})

navDropDownSkinConcern.addEventListener("mouseleave", () => {
    navDropDownSkinConcern.classList.remove("main-nav-js")
})


// Mobile Navigation Dropdown 
const hamburger = document.querySelector(".burger-menu"); 
const navMenu = document.querySelector(".mobile-navigation-container"); 

hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("mobile-nav-active");
})

// Mobile Serach Bar Dropdown 
const searchIcon = document.querySelector(".search-bar-mobile"); 
const search = document.querySelector(".mobile-serach-bar-container");

searchIcon.addEventListener("click", () =>{
    search.classList.toggle("search-active");
})

// Carousel 
// let i = 0; 
// let slides = []; 
// let slideFade = 6000; 

// Slide Images 
// slides[0] = "media/hero_image_1.jpg";
// slides[1] = "media/the_ordinary_slide.webp"; 
// slides[2] = "media/sunscreen_slide.webp"

// Slide Fade 
// function slideChange() {
//     document.slide.src = slides[i]; 
//     if(i < slides.length - 1) {
//         i++; 
//     }else{
//         i = 0; 
//     }
//     setTimeout("slideChange()", slideFade);
// }
// window.onload = slideChange; 


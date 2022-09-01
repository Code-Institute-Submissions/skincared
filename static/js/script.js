// User Profile Dropdown Toggle 
const userProfileIcon = document.getElementById('profile-icon');
const userProfileDropDown = document.querySelector('.user-profile-drop-down-menu'); 

userProfileIcon.addEventListener("click", function(){
    userProfileDropDown.classList.toggle("profile-active"); 
})

// const navHeading = document.querySelectorAll('.nav-heading'); 
// const navDropDown = document.querySelectorAll('.nav-drop-down'); 

// console.log(navHeading)
// console.log(navDropDown)

// for (i = 0; i < navHeading.length; i++) {
//     navHeading[i].addEventListener("click", function() {
//         for (i = 0; i < navDropDown.length; i++) {
//             this[i].classList.toggle("nav-active")
//         }
//     })
// }

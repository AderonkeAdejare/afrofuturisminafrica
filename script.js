
// // const openModalButtons = document.querySelectorAll('[data-modal-target]');
// let closeButton = document.querySelectorAll('[data-close-button]');
// let overlay = document.getElementById('overlay');

// overlay.addEventListener('click', () => {
//     let modals = document.querySelectorAll('.modal.active');
//     modals.forEach(modal => {
//         closeModal(modal);
//     });
// });

// closeButton.forEach(button => {
//     const modal = button.closest('.modal');
//     closeModal(modal);
// });

// function closeModal(modal){
//     if (modal == null) return
//     modal.classList.remove('active');
//     overlay.classList.remove('active');
// }

// function $(x) {return document.getElementById(x);}

// for pop up i couldn't complete
// $(doucment).ready(function() {
//     function showWindow(){
//         $('#modal').show();

//         $('html body').css('overflow', 'hidden');
//     }
//     // showWindow();

//     function hideWindow(){
//         $('#modal').hide();

//         $('html body').css('overflow', 'scroll');
//     }

//     // hideWindow();

//     setTimeout(showWindow, 2000);

//     $("#close-button").click(function() {
//         hideWindow();
//     })

// }

// );
// JS script for the accordion
document.addEventListener("DOMContentLoaded", function(event) {
    var acc = document.getElementsByClassName("faq-accordion");
    var panel = document.getElementsByClassName('faq-panel');
    for (var i = 0; i < acc.length; i++) {
        acc[i].onclick = function() {
            var setClasses = !this.classList.contains('active');
            setClass(acc, 'active', 'remove');
            setClass(panel, 'show', 'remove');
                if (setClasses) {
                    this.classList.toggle("active");
                    this.nextElementSibling.classList.toggle("show");
                }
        }
    }
    function setClass(els, className, fnName) {
        for (var i = 0; i < els.length; i++) {
            els[i].classList[fnName](className);
        }
    }
});

document.addEventListener("DOMContentLoaded", function(event) {
    var acc = document.getElementsByClassName("mobile-faq-menu");
    var panel = document.getElementsByClassName('mobile-faq-panel');
    for (var i = 0; i < acc.length; i++) {
        acc[i].onclick = function() {
            var setClasses = !this.classList.contains('active');
            setClass(acc, 'active', 'remove');
            setClass(panel, 'show', 'remove');
            if (setClasses) {
                this.classList.toggle("active");
                this.nextElementSibling.classList.toggle("show");
            }
        }
    }

    function setClass(els, className, fnName) {
        for (var i = 0; i < els.length; i++) {
            els[i].classList[fnName](className);
        }
    }
});

// // JS Script for the image modal pop-up for each floor plan
// var modal = document.getElementById('socMapImageModal');
// var images = document.getElementsByClassName('socMapImages');
// var modalImg = document.getElementById("img01");                                     // the image in the modal
// var captionText = document.getElementById("socMapImageModal-caption");               // and the caption in the modal

// // Go through all of the images with our custom class
// for (var i = 0; i < images.length; i++) {
//     var img = images[i];
//     // and attach our click listener for this image.
//     img.onclick = function(evt) {
//         modal.style.display = "block";
//         modalImg.src = this.src;
//         captionText.innerHTML = this.alt;
//     }
// }
// var span = document.getElementsByClassName("close")[0];
// span.onclick = function() {
//     modal.style.display = "none";
// }
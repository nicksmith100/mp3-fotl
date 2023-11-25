$(document).ready(function(){

    /* Display confirmation modal with dynamic confirm button */

    let confirmationModal = document.getElementById('modal-confirm');
    confirmationModal.addEventListener('show.bs.modal', function (event) {

        // Button that triggered the modal
        let button = event.relatedTarget;

        // Extract info from data-bs attributes
        let url = button.getAttribute('data-bs-url');
        let text = button.getAttribute('data-bs-text');

        // Update the modal's text content
        let modalText = confirmationModal.querySelector('.modal-text');
        modalText.innerHTML = `<strong class="text-danger"><i class="bi bi-exclamation-circle-fill" aria-hidden="true"> </i>${ text }</strong>`;

        // Update the modal's button content
        let modalConfirm = confirmationModal.querySelector('.btn-confirm');
        modalConfirm.href = url;

    });

    /* Date-and-time picker using flatpickr plugin */

    $(".showtime").flatpickr({
        enableTime: true,
        dateFormat: "d-m-Y H:i",
        minDate: "13-07-2023",
        maxDate: "16-07-2023"
    });

    /* Date picker using flatpickr plugin */

    $(".event-date").flatpickr({
        dateFormat: "d-m-Y",
        minDate: "01-07-2022",
    });

    $("#lineup-bios").on("click", ".flip-card", function(e) {
        if($(e.target).is("a")) {
            return true;
        } else { this.classList.toggle("flipped"); }
    });

    
});

/* Prevent overlapping images in Masonry layout.
Code from: https://kontext.tech/article/807/trigger-event-after-all-images-loaded */ 

let $grid = document.querySelector('.masonry-row');
let msnry = new Masonry($grid, {
    itemSelector: '.col',
    percentPosition: true
});
let $images = $grid.querySelectorAll('.card img');

Promise.all(
    Array.from($images).filter(img => !img.complete)
        .map(img => new Promise(resolve => { 
            img.addEventListener('load', resolve); 
            img.addEventListener('error', resolve);
        })
        )
).then(
    () => {
        msnry.layout();
    }
);
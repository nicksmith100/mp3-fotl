$(document).ready(function(){

    /* Display confirmation modal with dynamic confirm button
    Code from: https://getbootstrap.com/docs/5.0/components/modal/#varying-modal-content */

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

    /* Date-and-time pickers using flatpickr plugin
    Code from: https://flatpickr.js.org/examples */

    $(".showtime").flatpickr({
        enableTime: true,
        dateFormat: "d-m-Y H:i",
        minDate: event_start,
        maxDate: event_end
    });

    $(".event-date").flatpickr({
        dateFormat: "d-m-Y",
        minDate: "01-07-2022",
    });

    /* Event listener for flip-card function */

    $("#lineup-bios").on("click", ".flip-card", function(e) {
        if($(e.target).is("a")) {
            return true;
        } else { this.classList.toggle("flipped"); }
    });

    /* Prevent overlapping images in Masonry layout using imagesLoaded script
    Code from: https://masonry.desandro.com/layout#imagesloaded */ 

    let $grid = $('.masonry-row').masonry({
        itemSelector: '.flip-card',
        percentPosition: true
      });
        
    $grid.imagesLoaded().progress( function() {
        $grid.masonry('layout');
      });
    
});
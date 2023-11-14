$(document).ready(function(){

    /* Display confirmation modal with dynamic confirm button */

    let confirmationModal = document.getElementById('modal-confirm');
    confirmationModal.addEventListener('show.bs.modal', function (event) {

        // Button that triggered the modal
        let button = event.relatedTarget;

        // Extract info from data-bs-url attribute
        let url = button.getAttribute('data-bs-url');

        // Update the modal's text content
        let modalText = confirmationModal.querySelector('.modal-text');
        modalText.innerHTML = `<strong class="text-danger"><i class="bi bi-exclamation-circle-fill" aria-hidden="true"> </i>Are you sure? This action cannot be undone!</strong>`;

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

    function handler( event ) {
    var target = $( event.target );
    if ( target.is( "button" ) ) {
        target.children().toggleClass("bi-caret-down-fill bi-caret-up-fill");
        target.next().toggle(1000);
    }
    }
    
    $( "button" ).on( "click", handler );
    
});
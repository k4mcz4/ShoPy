document.addEventListener('DOMContentLoaded', () => {

        // Find the form element
        const formElement = document.getElementById('new-product-form');

        // Add a submit event listener to the form
        formElement.addEventListener('submit', function (e) {
        // Prevent the default form submission
        e.preventDefault();

        // Call the validateForm function
        const isFormValid = validateForm();

        // If the form is valid, submit it
        if (isFormValid) {
            formElement.submit();
        }
    });

// Get all the rows
let rows = document.querySelectorAll('.row');

// Add a click event listener to each row
rows.forEach(row => {
  row.addEventListener('click', () => {
    // Get the icon element
    const icon = row.querySelector('.icon');

    // If the row is already selected, deselect it and hide the icon
    if (row.classList.contains('is-selected')) {
      row.classList.remove('is-selected');
      icon.style.visibility = 'hidden';
    } else {
      // If the row is not selected, deselect all rows, hide all icons,
      // then select this row and show its icon
      rows.forEach(r => {
        r.classList.remove('is-selected');
        r.querySelector('.icon').style.visibility = 'hidden';
      });

      row.classList.add('is-selected');
      icon.style.visibility = 'visible';
    }
  });
});




    // Function to validate the form
    function validateForm() {
        var barcode = document.getElementById('barcode').value.trim();
        var productName = document.getElementById('product-name').value.trim();
        var price = document.getElementById('price').value.trim();

        if (barcode === '' || productName === '' || price === '') {
            alert('Please fill in all fields.');
            return false;
        }

        return true;
    }

    // Functions to open and close a modal
    function openModal($el) {
        $el.classList.add('is-active');
    }

    function closeModal($el) {
        $el.classList.remove('is-active');
    }

    function closeAllModals() {
        (document.querySelectorAll('.modal') || []).forEach(($modal) => {
            closeModal($modal);
        });
    }

    // Add a click event on buttons to open a specific modal
    (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
        const modal = $trigger.dataset.target;
        const $target = document.getElementById(modal);

        $trigger.addEventListener('click', () => {
            openModal($target);
        });
    });

    // Add a click event on various child elements to close the parent modal
    (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
        const $target = $close.closest('.modal');

        $close.addEventListener('click', () => {
            // Check if the form exists in the modal and prevent its submission
            const $form = $target.querySelector('form');
            if ($form) {
                $form.addEventListener('submit', (e) => {
                    e.preventDefault();
                });
            }

            closeModal($target);
        });
    });


  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Add a click event on each of them
  $navbarBurgers.forEach( el => {
    el.addEventListener('click', () => {

      // Get the target from the "data-target" attribute
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');

    });
  });
});

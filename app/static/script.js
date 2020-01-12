

// Journal Landing, enter a new journal if a click is detected in certain areas of the screen, also some other features
$(document).click(function(event) {
    $target = $(event.target);
    if((!$target.closest('#new-journal-disappear').length && !$target.closest('#new-journal-button').length) &&
        $('#new-journal-disappear').is(":visible")) {
        document.getElementById('submit-btn').click();
        document.getElementById('new_journal').getElementsByClassName("new-journal-input").value = '';
        $('#new-journal-disappear').hide();

    }
});

// One making the line to write a new journal appear/disappear if button is pressed
function newJournal() {
    var x = document.getElementById("new-journal-disappear");
    if (x.style.display === "block") {
    x.style.display = "none";
    } else {
    x.style.display = "block";
    }
}

function newSection() {
    var x = document.getElementById("new-section-disappear");
    if (x.style.display === "block") {
    x.style.display = "none";
    } else {
    x.style.display = "block";
    }
}

function newEntry()
{
    var x = document.getElementById("new-entry-disappear");
    if (x.style.display === "block") {
    x.style.display = "none";
    } else {
    x.style.display = "block";
    }
}

// To show and not show the select items
function minimiseSelect()
{
    var selectors = document.getElementsByClassName("select-expand");
    var minview = document.getElementById('select-minimise-view');
    for(var counter = 0; counter < selectors.length; counter++) {
        if (selectors[counter].style.display === "block") {
        selectors[counter].style.display = "none";
        minview.style.display = "block";
        $('#select-minimise-view').addClass('height-adjust-button');
        $('#entry-input').addClass('height-adjust-content');
        // To change the proportion (columns) of the screen it will take up
        $('#entry-input').removeClass('col-md-8');
        $('#entry-input').addClass('col-md-11');
        $('#entry-input').removeClass('col-4');
        $('#entry-input').addClass('col-11');
        // To make adjustments to padding and margin to the entry input when minimised
        $('#entry-input').addClass('minimise-view-content');
        } else {
        selectors[counter].style.display = "block";
        minview.style.display = "none";
        $('#select-minimise-view').removeClass('height-adjust-button');
        $('#entry-input').removeClass('height-adjust-content');
        $('#entry-input').addClass('col-md-8');
        $('#entry-input').removeClass('col-md-11');
        $('#entry-input').addClass('col-4');
        $('#entry-input').removeClass('col-11');
        $('#entry-input').removeClass('minimise-view-content');
        }
    }
}


// Navbar transition effect
$(document).ready(function() {
    $(window).scroll(function() {
          // checks if window is scrolled, adds/removes solid class
          if($(this).scrollTop() > 2) {
              $('.navbar_scrolled').addClass('solid');
          } else {
              $('.navbar_scrolled').removeClass('solid');
          }
    });
})


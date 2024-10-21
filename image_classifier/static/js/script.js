// $(document).ready(function () {
//     // Function to toggle between login and signup forms
//     function toggleSignUp(e) {
//         e.preventDefault(); // Prevent the default action

//         $('#login-form').hide();
//         $('#signup-form').show();
//         $('#signup-result').html(''); // Clear any previous messages
//     }

//     function toggleResetPswd(e) {
//         e.preventDefault(); // Prevent the default action

//         $('#login-form').hide();
//         $('#reset-form').show();
//         $('#signup-result').html(''); // Clear any previous messages
//     }

//     function toggleLogin(e) {
//         e.preventDefault(); // Prevent the default action

//         $('#signup-form').hide();
//         $('#login-form').show();
//         $('#signup-result').html(''); // Clear any previous messages
//     }

//     function toggleReset(e) {
//         e.preventDefault(); // Prevent the default action

//         $('#reset-form').hide();
//         $('#login-form').show();
//         $('#signup-result').html(''); // Clear any previous messages
//     }

//     // Bind click events
//     $('#btn-signup').click(toggleSignUp);
//     $('#cancel_signup').click(toggleLogin);
//     $('#forgot_pswd').click(toggleResetPswd);
//     $('#cancel_reset').click(toggleReset);
    
//     // Handle form submission via AJAX
//     $('#signup-form').on('submit', function (e) {
//         e.preventDefault(); // Prevent the default form submission

//         var formData = $(this).serialize(); // Serialize form data

//         $.ajax({
//             type: 'POST',
//             url: $(this).attr('action'),
//             data: formData,
//             success: function (response) {
//                 var resultDiv = $('#signup-result');
//                 resultDiv.html(''); // Clear previous messages

//                 if (response.status === 'success') {
//                     resultDiv.html('<div class="alert alert-success">' + response.message + '</div>');
//                 } else if (response.status === 'error') {
//                     resultDiv.html('<div class="alert alert-danger">' + response.message + '</div>');
//                 }
//             },
//             error: function () {
//                 $('#signup-result').html('<div class="alert alert-danger">An unexpected error occurred. Please try again later.</div>');
//             }
//         });
//     });
// });









// $(document).ready(function () {
//     // Function to toggle between forms
//     function toggleForm(showFormId, hideFormId) {
//         $(hideFormId).hide();
//         $(showFormId).show();
//         $('#form-result').html(''); // Clear any previous messages
//     }

//     // Bind click events for toggling forms
//     $('#btn-signup').click(function (e) {
//         e.preventDefault();
//         toggleForm('#signup-form', '#login-form');
//     });

//     $('#cancel_signup').click(function (e) {
//         e.preventDefault();
//         toggleForm('#login-form', '#signup-form');
//     });

//     $('#forgot_pswd').click(function (e) {
//         e.preventDefault();
//         toggleForm('#reset-form', '#login-form');
//     });

//     $('#cancel_reset').click(function (e) {
//         e.preventDefault();
//         toggleForm('#login-form', '#reset-form');
//     });

//     // Handle form submission via AJAX
//     function handleFormSubmission(formId) {
//         $(formId).on('submit', function (e) {
//             e.preventDefault(); // Prevent the default form submission

//             var formData = $(this).serialize(); // Serialize form data

//             $.ajax({
//                 type: 'POST',
//                 url: $(this).attr('action'),
//                 data: formData,
//                 success: function (response) {
//                     console.log('AJAX Response:', response); // Log the response
//                     var resultDiv = $('#form-result');
//                     resultDiv.html(''); // Clear previous messages

//                     if (response.status === 'success') {
//                         resultDiv.html('<div class="alert alert-success">' + response.message + '</div>');
//                         if (response.redirect) {
//                             window.location.href = response.redirect; // Redirect on success
//                         }
//                     } else if (response.status === 'error') {
//                         resultDiv.html('<div class="alert alert-danger">' + response.message + '</div>');
//                     }
//                 },
//                 error: function () {
//                     $('#form-result').html('<div class="alert alert-danger">An unexpected error occurred. Please try again later.</div>');
//                 }
//             });
//         });
//     }

//     // Bind AJAX form handling
//     handleFormSubmission('#login-form');
//     handleFormSubmission('#signup-form');

//     // Add CSRF token to AJAX requests
//     $.ajaxSetup({
//         headers: {
//             'X-CSRFToken': '{{ csrf_token }}'
//         }
//     });
// });








// $(document).ready(function () {
//     // Function to toggle between forms
//     function toggleForm(showFormId, hideFormId) {
//         $(hideFormId).hide();
//         $(showFormId).show();
//         $(showFormId).find('.form-result').html(''); // Clear any previous messages
//     }

//     // Bind click events for toggling forms
//     $('#btn-signup').click(function (e) {
//         e.preventDefault();
//         toggleForm('#signup-form', '#login-form');
//     });

//     $('#cancel_signup').click(function (e) {
//         e.preventDefault();
//         toggleForm('#login-form', '#signup-form');
//     });

//     $('#forgot_pswd').click(function (e) {
//         e.preventDefault();
//         toggleForm('#reset-form', '#login-form');
//     });

//     $('#cancel_reset').click(function (e) {
//         e.preventDefault();
//         toggleForm('#login-form', '#reset-form');
//     });

//     // Handle form submission via AJAX
//     function handleFormSubmission(formId) {
//         $(formId).on('submit', function (e) {
//             e.preventDefault(); // Prevent the default form submission

//             var formData = $(this).serialize(); // Serialize form data
//             var resultDiv = $(this).find('.form-result'); // Find the specific result area

//             $.ajax({
//                 type: 'POST',
//                 url: $(this).attr('action'),
//                 data: formData,
//                 success: function (response) {
//                     console.log('AJAX Response:', response); // Log the response
//                     resultDiv.html(''); // Clear previous messages

//                     if (response.status === 'success') {
//                         resultDiv.html('<div class="alert alert-success">' + response.message + '</div>');
//                         if (response.redirect) {
//                             window.location.href = response.redirect; // Redirect on success
//                         }
//                     } else if (response.status === 'error') {
//                         resultDiv.html('<div class="alert alert-danger">' + response.message + '</div>');
//                     }
//                 },
//                 error: function () {
//                     resultDiv.html('<div class="alert alert-danger">An unexpected error occurred. Please try again later.</div>');
//                 }
//             });
//         });
//     }

//     // Bind AJAX form handling
//     handleFormSubmission('#login-form');
//     handleFormSubmission('#signup-form');
//     handleFormSubmission('#reset-form'); // Ensure reset form is also handled

//     // Add CSRF token to AJAX requests
//     $.ajaxSetup({
//         headers: {
//             'X-CSRFToken': '{{ csrf_token }}'
//         }
//     });
// });







// $(document).ready(function () {
//     // Function to toggle between forms
//     function toggleForm(showFormId, hideFormId) {
//         $(hideFormId).hide();
//         $(showFormId).show();
//         $(showFormId).find('.form-result').html(''); // Clear any previous messages
//     }

//     // Bind click events for toggling forms
//     $('#btn-signup').click(function (e) {
//         e.preventDefault();
//         toggleForm('#signup-form', '#login-form');
//     });

//     $('#cancel_signup').click(function (e) {
//         e.preventDefault();
//         toggleForm('#login-form', '#signup-form');
//     });

//     $('#forgot_pswd').click(function (e) {
//         e.preventDefault();
//         toggleForm('#reset-form', '#login-form');
//     });

//     $('#cancel_reset').click(function (e) {
//         e.preventDefault();
//         toggleForm('#login-form', '#reset-form');
//     });

//     // Handle form submission via AJAX
//     function handleFormSubmission(formId) {
//         $(formId).on('submit', function (e) {
//             e.preventDefault(); // Prevent the default form submission

//             var formData = $(this).serialize(); // Serialize form data
//             var resultDiv = $(this).find('.form-result'); // Find the specific result area

//             $.ajax({
//                 type: 'POST',
//                 url: $(this).attr('action'),
//                 data: formData,
//                 success: function (response) {
//                     console.log('AJAX Response:', response); // Log the response
//                     resultDiv.html(''); // Clear previous messages

//                     if (response.status === 'success') {
//                         var message = response.message || 'Success'; // Default to 'Success' if message is undefined
//                         resultDiv.html('<div class="alert alert-success">' + message + '</div>');

//                         // Redirect after displaying the success message
//                         setTimeout(function() {
//                             if (response.redirect) {
//                                 window.location.href = response.redirect; // Redirect on success
//                             }
//                         }, 1000); // Adjust the delay as needed (1000ms = 1 second)
                        
//                     } else if (response.status === 'error') {
//                         var errorMessage = response.message || 'An error occurred'; // Default to generic error message if message is undefined
//                         resultDiv.html('<div class="alert alert-danger">' + errorMessage + '</div>');
//                     }
//                 },
//                 error: function () {
//                     resultDiv.html('<div class="alert alert-danger">An unexpected error occurred. Please try again later.</div>');
//                 }
//             });
//         });
//     }

//     // Bind AJAX form handling
//     handleFormSubmission('#login-form');
//     handleFormSubmission('#signup-form');
//     handleFormSubmission('#reset-form'); // Ensure reset form is also handled

//     // Add CSRF token to AJAX requests
//     $.ajaxSetup({
//         headers: {
//             'X-CSRFToken': getCookie('csrftoken')
//         }
//     });

//     // Function to get CSRF token from cookie
//     function getCookie(name) {
//         var cookieValue = null;
//         if (document.cookie && document.cookie !== '') {
//             var cookies = document.cookie.split(';');
//             for (var i = 0; i < cookies.length; i++) {
//                 var cookie = cookies[i].trim();
//                 // Check if this cookie's name matches the one we want
//                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
// });

$(document).ready(function () {
    // Function to toggle between forms
    function toggleForm(showFormId, hideFormId) {
        $(hideFormId).hide();
        $(showFormId).show();
        $(showFormId).find('.form-result').html(''); // Clear any previous messages
    }

    // Function to clear input fields
    function clearFormFields(formId) {
        $(formId).find('input[type="text"], input[type="password"], textarea').val('');
    }

    // Bind click events for toggling forms
    $('#btn-signup').click(function (e) {
        e.preventDefault();
        toggleForm('#signup-form', '#login-form');
    });

    $('#cancel_signup').click(function (e) {
        e.preventDefault();
        toggleForm('#login-form', '#signup-form');
    });

    $('#forgot_pswd').click(function (e) {
        e.preventDefault();
        toggleForm('#reset-form', '#login-form');
    });

    $('#cancel_reset').click(function (e) {
        e.preventDefault();
        toggleForm('#login-form', '#reset-form');
    });

    // Handle form submission via AJAX
    function handleFormSubmission(formId) {
        $(formId).on('submit', function (e) {
            e.preventDefault(); // Prevent the default form submission

            var formData = $(this).serialize(); // Serialize form data
            var resultDiv = $(this).find('.form-result'); // Find the specific result area

            $.ajax({
                type: 'POST',
                url: $(this).attr('action'),
                data: formData,
                success: function (response) {
                    console.log('AJAX Response:', response); // Log the response
                    resultDiv.html(''); // Clear previous messages

                    if (response.status === 'success') {
                        var message = response.message || 'Success'; // Default to 'Success' if message is undefined
                        resultDiv.html('<div class="alert alert-success">' + message + '</div>');

                        // Clear input fields
                        clearFormFields(formId);

                        // Display the success message for 3 seconds and then hide it
                        setTimeout(function() {
                            resultDiv.html(''); // Clear the message after 3 seconds

                            if (response.redirect) {
                                window.location.href = response.redirect; // Redirect on success
                            }
                        }, 3000); // 3000ms = 1 seconds

                    } else if (response.status === 'error') {
                        var errorMessage = response.message || 'An error occurred'; // Default to generic error message if message is undefined
                        resultDiv.html('<div class="alert alert-danger">' + errorMessage + '</div>');
                    }
                },
                error: function () {
                    resultDiv.html('<div class="alert alert-danger">An unexpected error occurred. Please try again later.</div>');
                }
            });
        });
    }

    // Bind AJAX form handling
    handleFormSubmission('#login-form');
    handleFormSubmission('#signup-form');
    handleFormSubmission('#reset-form'); // Ensure reset form is also handled

    // Add CSRF token to AJAX requests
    $.ajaxSetup({
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    });

    // Function to get CSRF token from cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Check if this cookie's name matches the one we want
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Handle logout prompt
    $('#logout-button').click(function () {
        if (confirm('Are you sure you want to log out?')) {
            window.location.href = '/login/'; // Redirect to sign-in page
        }
    });
});

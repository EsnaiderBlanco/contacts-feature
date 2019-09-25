/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
  $(".sidenav").width("250px");
  $(".mainnav").css( {marginLeft : "250px" });
  $(".mainnav").removeClass("col-12");
  $(".mainnav").addClass("col-10");
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  $(".sidenav").width("0");
  $(".mainnav").css({marginLeft : "0" });
  $(".mainnav").removeClass("col-10");
  $(".mainnav").addClass("col-12");
}

$(document).on("click", "#edit_contact", function () {
  var name = $(this).closest('tr').children('td.column1').text();
  var phone_number = $(this).closest('tr').children('td.column2').text();
  var email = $(this).closest('tr').children('td.column3').text();
  var description = $(this).closest('tr').children('td.column4').text();  
  var id = $(this).closest('tr').children('td.column5').text(); 
  
  $(".modal-body #name").val(name);
  $(".modal-body #phone_number").val(phone_number);
  $(".modal-body #email").val(email);
  $(".modal-body #description").val(description);
  $(".modal-body #id").val(id);
});

$(document).on("click", "#delete_contact", function () { 
  var id = $(this).closest('tr').children('td.column5').text(); 
  $(".modal-body #id").val(id);
});
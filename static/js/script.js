$(document).ready(function () {
  $(".navbar-toggler").on("click", function () {
    $(this).toggleClass("open");
    $(".navbar-nav").toggleClass("open");
    $("body").toggleClass("open");
  });
});

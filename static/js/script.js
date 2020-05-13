$(document).ready(function () {
  $(".navbar-toggler").on("click", function () {
    $(this).toggleClass("open");
    $(".navbar-nav").toggleClass("open");
    $("body").toggleClass("open");
  });

  $("#up").on("click", function () {
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      1000
    );
  });
});

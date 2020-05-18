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

  $(".theme-toggler li").on("click", function () {
    $(this).toggleClass("active");
    $("body").toggleClass("dark");
  });

  // $(document).ready(function () {
  //   $("#myInput").on("keyup", function () {
  //     var value = $(this).val().toLowerCase();
  //     $("#newsDeck .post-data").filter(function () {
  //       // $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
  //     });
  //   });
  // });
});

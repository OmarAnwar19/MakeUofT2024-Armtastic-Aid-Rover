$("button").click(function (e) {
  e.preventDefault();
  $.ajax({
    url: $(this).data("url"),
    type: "POST",
    data: {},
    success: function (response) {
      alert(response.status);
    },
    error: function (xhr, errmsg, err) {
      console.log(xhr.status + ": " + xhr.responseText);
    },
  });
});

function loadRandomImage(){
  $.get("/api/v1/raw/", function(d, s){
    if (d.filename)
    {
      $("#crop-container").croppie("bind",{ url: d.filename});
      $("#rawId").val(d.id);
    }
  });
}

function saveCrop(){
  $("#crop-container").croppie("result", "canvas", "viewport").then(function (resp) {
    if (resp){
      $.post("/api/v1/processed/"+$("#rawId").val(),{"data": resp})
        .done(loadRandomImage);
    }
  });
}

var Crop = (function(){
  function init() {
    $("#crop-container").croppie({
      viewport: { width: 155, height: 35, type: "square"},
      boundary: { width: 800, height: 600},
      mouseWheelZoom: true
    });
    loadRandomImage(); 
  }

  return { init: init };
})();
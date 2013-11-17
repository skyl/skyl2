(function(){
  var $ = django.jQuery;
  var w = window.open("","","scrollbars=1,left=840,width=580,height=900");
  changef = function(ev){
    var t = $(ev.currentTarget);
    var s = t.val();
    $.ajax({
      url: "/preview_rst",
      type: "POST",
      data: s,
      processData: false,
      success: function(data) {
        w.document.body.innerHTML = "";
        w.document.write(data);
      }
    });
  };
  $(function(){
    window.onunload = function(){
      w.close();
    };
    $('textarea#id_content').change(changef).change();
  });
})();

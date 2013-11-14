(function(){
  var $ = django.jQuery;
  var w = window.open("","","left=840,width=680,height=900");
  keyupf = function(ev){
    t = $(ev.currentTarget);
    s = t.val();
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
    $('textarea#id_content').keyup(keyupf).keyup();
  });
})();

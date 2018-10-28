//ドロワーメニュー
$(document).ready(function() {
  $(".drawer").drawer();
});





//背景色が変更された時の挙動
$(function(){
  $('input[name="radio_bgcolor"]:radio').change(function(){
    var radio_color = $(this).val();
    if(radio_color == "#fff8dc"){
      $("#title").removeClass("bg-lightblue")
      $("#title").removeClass("bg-black")
      $("#title").addClass("bg-cream")
    }
    if(radio_color == "#f0f8ff"){
      $("#title").removeClass("bg-cream")
      $("#title").removeClass("bg-black")
      $("#title").addClass("bg-lightblue")
    }
    console.log();
    renderer.setClearColor(radio_color, 1.0);  //変更された背景色
    if(radio_color == "#000000"){   //背景色が黒の時は文字色を白にする
      $("#operation-manual").addClass("whitecoolor");
      $("#description").addClass("whitecoolor");
      $("#op_label").addClass("whitecoolor");
      $("#desc_label").addClass("whitecoolor");
      $("#hide_label").addClass("whitecoolor");
      $("#title").addClass("whitecoolor");
      $("#title").removeClass("bg-cream")
      $("#title").removeClass("bg-lightblue")
      $("#title").addClass("bg-black");
    }else{  //それ以外の色に変わったらクラスを消す
      $("#operation-manual").removeClass("whitecoolor");
      $("#description").removeClass("whitecoolor");
      $("#op_label").removeClass("whitecoolor");
      $("#desc_label").removeClass("whitecoolor");
      $("#hide_label").removeClass("whitecoolor");
      $("#title").removeClass("whitecoolor");
    }
  })
})
// 背景色に関する項目ここまで

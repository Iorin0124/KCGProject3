// アコーディオンメニュー
$(function(){
  $('.accordion > dl > dt').on('click',function(){
    var Dopenclass = $(this).attr('class');
    $(this).next('dd').slideToggle();
    if(!Dopenclass){
      $(this).addClass('dopen');
    }else{
      $(this).removeClass('dopen');
    }
  });
});

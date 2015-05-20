</div>

<footer id="contact" class="site-footer">
  <h2>Come meet with us and develop a legal plan for your business</h2>
  <hr>
  <div class="row">
    <div class='map'><a href="https://www.google.ca/maps/search/51+Melcher+Street+First+Floor+Boston,+MA+02210/@42.3498416,-71.0502411,17z/data=!3m1!4b1?hl=en">Map</a></div>
    <div class='physical-address'>
      <h4>Physical Address</h4>
      <address>
        51 Melcher Street<br>
        First Floor<br>
        Boston, MA 02210
      </address>
    </div>
    <div class='postal-address'>
      <h4>Postal Address</h4>
      <address>
        PO Box 51476<br>
        Boston, MA 02205<br>
        &nbsp;
      </address>
    </div>
    <div class="grid-3">
      <h4>Telephone</h4>
      <p><a href="tel:617.765.4222">617-765-4222</a></p>
    </div>
    <div class="grid-3">
      <h4>Facsimile</h4>
      <p><a href="tel:484.993.2271">484-993-2271</a></p>
    </div>
  </div>
  <hr>
  <ul class="social-links">
    <li>
      <a href="http://bostonbuilt.org/" target="_blank"><img src="img/BuiltinBoston.png"></a>
    </li>
    <li>
      <a href="http://creativecommons.org/licenses/by/3.0/" target="_blank"><img src="img/cc.small.png"></a>
    </li>
    <li>
      <a href="http://creativecommons.org/licenses/by/3.0/" target="_blank"><img src="img/by.small.png"></a>
    </li>
    <li>Copyright 2015, Fort Point Legal PC</li>
    <li class='right'><a href="/policy">Policy & Disclaimer</a></li>
  </ul>
</footer>

<script src="js/script.js"></script>
<script src="js/jquery.js"></script>
<script>
  // Scrolling to anchor points

  function tastyScroll(target){
   var $target = $(target);
   if(!$target.offset()) {
    return;
   }
   var offset = $target.offset().top - 200;
   $('html, body').stop().animate({
       'scrollTop': offset
   }, 900, 'swing', function () {
       window.location.hash = target;
   });
  }
  // Scrolling to anchor points
  $('a[href^="#"]').on('click',function (e) {
   e.preventDefault();
   var target = this.hash;
   tastyScroll(target);
  });
  $(window).on('load', function (e){
    if (window.location.hash) {
      tastyScroll(window.location.hash);
    }
  });
</script>
</body>

</html>

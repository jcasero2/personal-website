import React from 'react';
import ReactDOM from 'react-dom';
// import Likes from './likes';

// This method is only called once
// Insert the likes component into the DOM
// <Likes url="/api/v1/p/1/likes/" />,
// ReactDOM.render(
//   <Posts />,
//   document.getElementById('reactEntry'),
// );
$(document).ready(function() {
  $(".menu-icon").on("click", function() {
    $("nav ul").toggleClass("showing");
  });
});

// Scrolling Effect
$(window).on("scroll", function() {
  if($(window).scrollTop()) {
    $('nav').addClass('white');
  } else {
    $('nav').removeClass('white');
  }
});

$(document).on('click', '.homeMoreContainer', function() {
    $([document.documentElement, document.body]).animate({
        scrollTop: $(".resumeContainer").offset().top
    }, 2000);
});

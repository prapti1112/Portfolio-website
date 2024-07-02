var colors = ["#0ae448","#ff8709", "#9d95ff", "#00bae2"];
gsap.set(".cards li", {
	backgroundColor: (i) => colors[i % colors.length],
   y: (i) => i * 50
  });
  
  
  gsap.to(".cards li", {
	duration: 5,
	ease: "none",
	y: "+=500", //move each box 500px to right
	modifiers: {
	  y: gsap.utils.unitize(y => parseFloat(y) % 500) //force x value to be between 0 and 500 using modulus
	},
	repeat: -1
  });
  
  

//   Horizontal Showcase Display
// var slider = new Swiper(".slider", {
// 	effect: 'coverflow',
// 	grabCursor: true,
// 	centeredSlides: true,
// 	loop: true,
// 	slidersPerView: 10,
// 	coverflowEffect: {
// 		rotate: 0,
// 		stretch: 0,
// 		depth: 100,
// 		modifier: 2.5
// 	},
// 	pagination: {
// 		el: ".swiper-pagination",
// 		clickable: true,
// 	},
// 	navigation: {
// 		nextEl: ".swiper-button-next",
// 		prevEl: ".swiper-button-prev",
// 	}
// });

var project_iteration = 0;
var project_carousel = $("#projects .carousel"),
    project_items = $("#projects .item"),
    project_currdeg  = 0;

$("#projects .next").on("click", { d: "n" }, rotate_project);
$("#projects .prev").on("click", { d: "p" }, rotate_project);

setInterval(function () {
	project_iteration++;
	// console.log( `Iteration updated ${project_iteration}` );
	rotate_project({ "data": {"d": "n"} });
}, 3000);

function rotate_project(e){
  if(e.data.d=="n"){
    project_currdeg = project_currdeg - 30;
  }
  if(e.data.d=="p"){
    project_currdeg = project_currdeg + 30;
  }
  project_carousel.css({
    "-webkit-transform": "rotateY("+project_currdeg+"deg)",
    "-moz-transform": "rotateY("+project_currdeg+"deg)",
    "-o-transform": "rotateY("+project_currdeg+"deg)",
    "transform": "rotateY("+project_currdeg+"deg)"
  });
    project_items.css({
    "-webkit-transform": "rotateY("+(-project_currdeg)+"deg)",
    "-moz-transform": "rotateY("+(-project_currdeg)+"deg)",
    "-o-transform": "rotateY("+(-project_currdeg)+"deg)",
    "transform": "rotateY("+(-project_currdeg)+"deg)"
  });
}


var blog_iteration = 0;
var blog_carousel = $("#blogs .carousel"),
    blog_items = $("#blogs .item"),
    blog_currdeg  = 0;

$("#blogs .next").on("click", { d: "n" }, rotate_blog);
$("#blogs .prev").on("click", { d: "p" }, rotate_blog);

setInterval(function () {
	blog_iteration++;
	// console.log( `Iteration updated ${blog_iteration}` );
	rotate_blog({ "data": {"d": "n"} });
}, 3000);

function rotate_blog(e){
  if(e.data.d=="n"){
    blog_currdeg = blog_currdeg - 30;
  }
  if(e.data.d=="p"){
    blog_currdeg = blog_currdeg + 30;
  }
  blog_carousel.css({
    "-webkit-transform": "rotateY("+blog_currdeg+"deg)",
    "-moz-transform": "rotateY("+blog_currdeg+"deg)",
    "-o-transform": "rotateY("+blog_currdeg+"deg)",
    "transform": "rotateY("+blog_currdeg+"deg)"
  });
    blog_items.css({
    "-webkit-transform": "rotateY("+(-blog_currdeg)+"deg)",
    "-moz-transform": "rotateY("+(-blog_currdeg)+"deg)",
    "-o-transform": "rotateY("+(-blog_currdeg)+"deg)",
    "transform": "rotateY("+(-blog_currdeg)+"deg)"
  });
}
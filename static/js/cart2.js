

// /* ---------------------------------------------------------------------------------------*/
var adv=[
	{
		image :"/static/images/slider1.jpg",
		link : "http://localhost:8000/Man/T-shirt%20Man",
	},
	{
		image : "/static/images/slider2.jpg",
		link : "http://localhost:8000/Product%20Coupons/Premium",
	},
	{
		image : "/static/images/slider3.jpg",
		link : "http://localhost:8000/Electronic/Cell%20Phone",
	},
	{
		image :"/static/images/slider4.jpg",
		link :"http://localhost:8000/Home/Chandelier",
	},
]

var index = 1;
var slaytCount = adv.length;
var interval;

var settings={
	duration:"2000"
}
init(settings);
function init(settings){
	interval=setInterval(function(){
	if(slaytCount == index+1){
		index = -1;
	}
	showSlide(index);

	index++;
showSlide(index);
},settings.duration)
}



function showSlide(i){
	index=i;
	if (i<0) {
        index = slaytCount - 1;
    }
    if(i >= slaytCount){
        index =0;
    }
	document.querySelector('.card-img-top').setAttribute('src',adv[index].image);
	document.querySelector('.card-link').setAttribute('href',adv[index].link);
}


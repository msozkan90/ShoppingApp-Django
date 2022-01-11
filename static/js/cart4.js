
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action)
		}else{
			updateUserOrder(productId, action)
		}
      
	})
    
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		        location.reload()
            console.log(data)
		});
}







// // const deneme=document.getElementsByClassName("update-cart");
// // eventListeners();
// // function eventListeners(){
// //     for (i = 0; i < deneme.length; i++) {
// // 	deneme[i].addEventListener("click",function(e){
// // 		console.log("DENEME ÇALIŞTI");
// //         e.preventDefault();
// // 	})
// // }}
// var updateBtns = document.getElementsByClassName('update-cart')

// for (i = 0; i < updateBtns.length; i++) {
// 	updateBtns[i].addEventListener('click', function(e){
		
// 		var productId = this.dataset.product
// 		var action = this.dataset.action
//         data ={"productId":productId, "action":action};
//         link="http://localhost:8000/update_item/";
// 		console.log('productId:', productId, 'Action:', action)
// 		console.log('USER:', user)
//         const updateUserOrders = new updateUserOrder()
// 		if (user == 'AnonymousUser'){
// 			addCookieItem(productId, action)
// 		}
// 		else{
// 			url="https://jsonplaceholder.typicode.com/albums"
//             console.log(link);
//             console.log(data);
// 			updateUserOrders.update(link,data)
// 			updateUserOrders.update2(url,data)
//             .then(result=> console.log(result))
//             //.catch(err => console.log(err))
			
// 		}
// 		//e.preventDefault();
// 	})
// }

// function updateUserOrder(productId, action){
// 	console.log('User is authenticated, sending data...')

// 	var url = 'update_item/'

// 	fetch(url, {
// 			method:'POST',
// 			headers:{
// 				'Content-Type':'application/json',
// 				'X-CSRFToken':csrftoken,
// 			}, 
// 			body:JSON.stringify({'productId':productId, 'action':action})
// 		})
// 		.then((response) => {
// 		//    return response.json();
// 		   console.log(response.json())
// 		})
// 		.then((data) => {
// 			console.log(data)
// 		    //location.reload()
			
// 		})
// 		.catch(err => console.log(err))
		
// }




function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}

/* ---------------------------------------------------------------------------------------*/
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
	duration:"2500"
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
//---------------------------------------------------------------------------------------


// /* ---------------------------------------------------------------------------------------*/


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
// 		console.log("DENEME")
// 		var productId = this.dataset.product
// 		var action = this.dataset.action
// 		console.log('productId:', productId, 'Action:', action)
// 		console.log('USER:', user)
//         const updateUserOrders = new updateUserOrder(productId, action)
// 		if (user == 'AnonymousUser'){
// 			addCookieItem(productId, action)
// 		}
// 		else{
            
// 			updateUserOrders.update('/update_item/',{"productId":productId, "action":action})
//             .then(result=> {console.log(result)})
//             //.catch(err => console.log(err))
			
// 		}
// 		e.preventDefault();
// 	})
// }

// // function updateUserOrder(productId, action){
// // 	console.log('User is authenticated, sending data...')

// // 	var url = 'update_item/'

// // 	fetch(url, {
// // 			method:'POST',
// // 			headers:{
// // 				'Content-Type':'application/json',
// // 				'X-CSRFToken':csrftoken,
// // 			}, 
// // 			body:JSON.stringify({'productId':productId, 'action':action})
// // 		})
// // 		.then((response) => {
// // 		//    return response.json();
// // 		   console.log(response.json())
// // 		})
// // 		.then((data) => {
// // 			console.log(data)
// // 		    //location.reload()
			
// // 		})
// // 		.catch(err => console.log(err))
		
// // }




// function addCookieItem(productId, action){
// 	console.log('User is not authenticated')

// 	if (action == 'add'){
// 		if (cart[productId] == undefined){
// 		cart[productId] = {'quantity':1}

// 		}else{
// 			cart[productId]['quantity'] += 1
// 		}
// 	}

// 	if (action == 'remove'){
// 		cart[productId]['quantity'] -= 1

// 		if (cart[productId]['quantity'] <= 0){
// 			console.log('Item should be deleted')
// 			delete cart[productId];
// 		}
// 	}
// 	console.log('CART:', cart)
// 	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
// 	location.reload()
// }


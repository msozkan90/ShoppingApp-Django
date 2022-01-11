class updateUserOrder{
    constructor(productId,action){
        this.productId=productId;
        this.action=action;
       // this.url='/update_item/'
    }
    update(url,data){
        return new Promise((resolve,reject)=>{
            fetch(url,{
            method:'POST',
            body:JSON.stringify(data),
			headers:{
				'Content-Type':'application/json;charset=UTF-8',    
				'X-CSRFToken':csrftoken,
			} 
			//body:JSON.stringify({'productId':this.productId, 'action':this.action})   
		})
		.then((response) => response.json())
		.then((data)=> resolve(data))
		//.catch(err => reject(err));
//location.reload())
		//    return response.json();response.json)
            })   
    }
}
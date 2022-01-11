function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getToken('csrftoken');
console.log("CSRFTOKEN:",csrftoken)
class updateUserOrder{
    constructor(productId,action){
        this.productId=productId;
        this.action=action;

       // this.url='/update_item/'
    }    
    // async post(data){
    //     // location.reload()
    //     // console.log("at")

    //     //let data={"productId":data1,"action":data2}
    //     const response = await fetch("http://localhost:8000/update_item/",{
    //                 method: 'POST',
    //                 body: JSON.stringify(data),
    //                 headers: {
    //                   "Content-type": "application/json",
    //                   "Accept": "application/json",
    //                   "X-CSRFToken":csrftoken,
                      
    //                 }
    //             }); // Response Object

    //     const responsedata = await response.text();
        
    //     return JSON.stringify(data);
        
   // "https://jsonplaceholder.typicode.com/albums/2"
    
    update(url){
            //data={'productId':this.productId, 'action':this.action}
        return new Promise(()=>{
            fetch(url,{
            method:'POST',
           // body:data,
			headers:{
				'Content-Type':'application/json',    
				'X-CSRFToken':csrftoken,
			} ,
			body:JSON.stringify({'productId':this.productId, 'action':this.action})   
            
		})
		.then(response => response.text())
        .then(data => console.log(data))
    })}
     
    update2(url){
        //data={'productId':this.productId, 'action':this.action}
    return new Promise(()=>{
        fetch(url,{
        method:'POST',
       // body:data,
        headers:{
            'Content-Type':'application/json',    
            'X-CSRFToken':csrftoken,
        } ,
        body:JSON.stringify({userId:4332,title:"Maltepe"})   
        
    })
    .then(response => response.text())
    .then(data => console.log(data))
})}





        //     async response => {
        //     try {
        //         console.log(url)
        //      const data = await response.json()
        //      console.log('response data?', data)
        //    } catch(error) {
        //      console.log('Error happened here!')
        //      console.error(error)
        //    }
		//.then((data)=> resolve(data))
        
		//.catch(err => reject(err));
//location.reload())
		//    return response.json();response.json)
              
    
}

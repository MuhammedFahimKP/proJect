const form = document.getElementById("myform");
const error = document.getElementById("error");
form.addEventListener('submit',(e)=>{
    if(!getSelectedRadio()){
    
        error.style.display="block";
        error.innerHTML="<p>Please Select a Address</p>"
        e.preventDefault();
        

       
        
    } 
})



function getSelectedRadio() {
    var selected = document.querySelector('input[name="address"]:checked');
    if (selected) {            
            return true 
    } 
        return false
}
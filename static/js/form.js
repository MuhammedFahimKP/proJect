const fname = document.getElementById('fname');  
const lname = document.getElementById('lname');
const email = document.getElementById('email');
const pass1 = document.getElementById('pass1');
const pass2 = document.getElementById('pass2');
const error = document.getElementsByClassName('error')
const form  = document.getElementById('form')
const btn   = document.getElementById('submitbutton')


form.addEventListener('submit',(e)=>{

    let c = 0;

    if (!validName()){
        error[0].style.display = "block"
        error[0].innerHTML="<p>Please Provid valid name</p>"
        c+=1;
    }
    
    if (!validEmail()){
        error[1].style.display = "block"
        error[1].innerHTML="<p>Please Provid valid Email</p>"
        c+=1;
    }
    if(!validPass()){
        error[2].style.display = "block"
        error[2].innerHTML="<p>Password Must be alphanumric  </p>"
        c+=1;
    }
    if(pass1.value.length < 8 ) {
        error[3].style.display = "block"
        error[3].innerHTML="<p>Password Must be 8 characters </p>"
        c+=1;
    }
       
    

    if(pass1.value != pass2.value){

        error[4].style.display = "block"
        error[4].innerHTML="<p>Password Not matching</p>"
        c+=1;
    }

    if(c>0){
        e.preventDefault();
    }

})

 
function validName(){
    regex = /^[a-zA-Z ]{2,30}$/;
    return regex.test(fname.value) &&  regex.test(lname.value); 

}
function validEmail(){
    regex =  /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return regex.test(email.value);
}
function validPass(){
    regex = /^[a-zA-Z0-9]+$/;
    return regex.test(pass1.value)
}



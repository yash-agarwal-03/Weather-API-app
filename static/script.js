function alert(){
    var alertBox = document.getElementById("alertbox");
    var alertmsg = document.getElementById("alert");
    var error=alertmsg.textContent;
    console.log('error - ',error)

    alertBox.classList.add("show");
    setTimeout(()=>{
                    alertBox.classList.remove("show");
                    alertBox.classList.add("hide");        
                    },3000);
}
window.onload=alert;

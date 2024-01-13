document.addEventListener("DOMContentLoaded", function(){

    

    window.addEventListener("scroll", function(){
        navba = document.getElementById("navbar")
        mainContent = document.getElementById("main")
        if (this.window.scrollY>=376){
            
            mainContent.classList.add("mt-5")
            navba.classList.add("fixed-top")
        }
        else{
            mainContent.classList.remove("mt-5")
            navba.classList.remove("fixed-top")
        }
    })



    const mobileContact = document.getElementById("mobile-contact1")
    mobileContact.addEventListener("click",()=>{
      const mobileContact = "9880017459";

      navigator.clipboard.writeText(mobileContact)
          .then(() => {
              console.log('Text successfully copied to clipboard');
          })
          .catch((error) => {
              console.error('Unable to copy text to clipboard', error);
          });
    })
    const mobileContact2 = document.getElementById("mobile-contact2")
    mobileContact2.addEventListener("click",()=>{
      const mobileContact = "8067188204";

      navigator.clipboard.writeText(mobileContact)
          .then(() => {
              console.log('Text successfully copied to clipboard');
          })
          .catch((error) => {
              console.error('Unable to copy text to clipboard', error);
          });
    })
})

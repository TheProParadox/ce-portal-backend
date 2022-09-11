const btn=document.querySelector("#button1");
const form= document.querySelector("#main");
var i=1;
btn.addEventListener('click',target=>{
    const temp=form.firstElementChild;
    target.preventDefault()
    console.log(temp);
    console.log(form);
    document.getElementById("num").value = i
    form.innerHTML+=`<div id="a">
    <h1>Candidate ${i+1}</h1>
    <p>
        <label for="id_name">Name:</label>
        <input type="text" name="name${i}" maxlength="50" required="" id="id_name">


    </p>
    <p>
        <label for="id_email">Email:</label>
        <input type="email" name="email${i}" maxlength="254" required="" id="id_email">
    </p>
</div>`;
    i++;
})
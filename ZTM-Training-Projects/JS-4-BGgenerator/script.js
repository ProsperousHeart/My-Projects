var css = document.querySelector("h3");
var color1 = document.querySelector(".color1");  // class selector just like in CSS
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient");

// TODO:  Color picker on FireFox doesn't automatically detect color picker

/*console.log(css);
console.log(color1);
console.log(color2);*/
//console.log(body);

function setGradient() {
    // console.log(event.value);
    body.style.background =
        "linear-gradient(to right, "
        + color1.value
        + ", "
        + color2.value
        + ")";
    css.textContent = body.style.background + ";";
}

// listen to event where we notice user's actions
color1.addEventListener("input", setGradient)
color2.addEventListener("input", setGradient)

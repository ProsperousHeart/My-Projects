var input = document.getElementById("userinput");
var btn = document.getElementById("enter");
// var ul = document.querySelector("ul");
var ul = document.getElementById("ShoppingList");
//var items = document.querySelectorAll("li");
var clearBtn = document.getElementById("clear");


function inputLength() {
    return input.value.length;
}

function addListenerClick() {
    // console.log("Click is working")
    // if (input.value.length > 0) {
    if (inputLength() > 0) {
        // console.log(input.value);
        createListElem();
    }
}

function addListAfterKeyPress(event) {
    // console.log(event);
    // if (input.value.length > 0 && event.keyCode === 13) { // may also try event.which == 13 OR event.code === "Enter"
    if (inputLength() > 0 && event.keyCode === 13) {
        // console.log(input.value);
        createListElem();
    }
}

function delParentNodeOnClick(itm) {
    // console.log(itm);
    this.parentNode.parentNode.remove();
}

function strikeItem() {
    this.parentNode.parentNode.classList.toggle("done-txt");
    if (this.innerText === "Done"){
        this.innerText = "Undo";
    } else {
        this.innerText = "Done";
    };
    this.classList.toggle("btn-success");
    this.classList.toggle("btn-outline-warning");
}

function createListElem() {
    var wrapper = document.createElement("div");
    wrapper.classList.add("item");

    var li = document.createElement("li");
    // console.log(item);
    li.appendChild(document.createTextNode(input.value));
    // console.log(item);

    var btnWrapper = document.createElement("div");
    btnWrapper.classList.add("btn-wrapper");

    // create DONE button
    // var doneBtn = document.createElement("button");
    // doneBtn.innerHTML = "Done";
    var doneBtn = document.createElement("a");
    var btnText = document.createTextNode("Done");
    doneBtn.appendChild(btnText);
    //doneBtn.classList.add("btn", "btn-success");
    doneBtn.classList.add("btn");
    doneBtn.classList.toggle("btn-success");
    //console.log(doneBtn);

    doneBtn.addEventListener("click", strikeItem);
    btnWrapper.appendChild(doneBtn);

    // create DEL button
    var delBttn = document.createElement("button");
    //btnText = document.createTextNode("Delete");
    //delBttn.appendChild(btnText);
    delBttn.innerHTML = "Delete";
    delBttn.classList.add("btn", "btn-outline-danger");
    delBttn.addEventListener("click", delParentNodeOnClick);
    btnWrapper.appendChild(delBttn);

    wrapper.appendChild(li);
    wrapper.appendChild(btnWrapper);
    ul.appendChild(wrapper);  // add list item to UL
    input.value = "";
}

function clearList() {
    ul.innerHTML = "";
}

// add event listener to button
btn.addEventListener("click", addListenerClick)

// add event listener to button
input.addEventListener("keypress", addListAfterKeyPress)

clearBtn.addEventListener("click", clearList);

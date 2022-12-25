var database = [
    {
        user: "user1",
        pw: "secret"
    },
    {
        user: "user2",
        pw: "secret1"
    },
    {
        user: "user3",
        pw: "secret3"
    }
];

var newsfeed = [
    {
        user: "Jane",
        timeline: "So tired from learning."
    },
    {
        user: "Bob",
        timeline: "JS - magic!"
    }
]

function isUserValid(username, password) {
    for (var i=0; i<database.length; i++) {
        if(database[i].user === userNamePrompt &&
            database[i].pw === pwPrompt) {
            return true;
        }
    }
    return false;
}

function signIn(user, pw) {
//    if (user === null || pw === null) {
//        alert("Sorry, please provide credentials.");
//    } else if (user === database[0].user && pw === database[0].pw) {
//        console.log(newsfeed);
//    } else {
//        alert("Sorry, wrong credentials.");
//    }
    if (isUserValid(user, pw)) {
        console.log(newsfeed);
    } else {
        alert("Sorry, wrong credentials.");
    }
}



var userNamePrompt = prompt("What's your username?");
//console.log(userNamePrompt);
var pwPrompt = prompt("What's your password?");
//console.log(pwPrompt);

signIn(userNamePrompt, pwPrompt);

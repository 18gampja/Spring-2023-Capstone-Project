// imageOverride image list:
var imgList = ["https://www.akc.org/wp-content/uploads/2015/03/so-you-want-to-breed-dogs-500x500.jpg", "https://d2zp5xs5cp8zlg.cloudfront.net/image-29200-800.jpg", "https://cdn.sanity.io/images/4ij0poqn/production/b31f90398e29954c91dbfc95b4208d223a172aa4-500x500.jpg", "https://pawsitivepotential.com/wp-content/uploads/2016/05/Tongue-Kitten-500x500_t.jpg", "https://petcureoncology.com/wp-content/uploads/shutterstock_1218542488.jpg", "https://d2zp5xs5cp8zlg.cloudfront.net/image-29642-800.jpg"];

// Detect if the mouse is being held down
addEventListener("mousedown", (event) => {});
addEventListener("mouseup", (event) => {});

var mouseDown = 0;
var mouseUp = 1;

onmousedown = (event) => {
    mouseDown = 1;
    mouseUp = 0;
};
onmouseup = (event) => {
    mouseDown = 0;
    mouseUp = 1;
};
//

// WASD Key detector
document.addEventListener("DOMContentLoaded", function(event) {
    const wKeyDiv = document.querySelector(".wKey");
    const aKeyDiv = document.querySelector(".aKey");
    const sKeyDiv = document.querySelector(".sKey");
    const dKeyDiv = document.querySelector(".dKey");

    if (wKeyDiv && aKeyDiv && sKeyDiv && dKeyDiv) {
        document.addEventListener("keydown", function(event) {
            switch (event.code) {
                case "KeyW":
                    if (wKeyDiv.dataset.state == "inactive") {
                        wKeyDiv.dataset.state = "active"
                        wKeyDiv.style.backgroundColor = "rgba(0, 255, 0, 0.5)";
                        wKeyDiv.style.border = ".15rem solid rgba(0, 50, 0, 0.75)";
                        wKeyDiv.style.fontWeight = "bold";
                        wKeyDiv.style.transform = "translateY(-.25rem)";
                    }
                    break;
                case "KeyA":
                    if (aKeyDiv.dataset.state == "inactive") {
                        aKeyDiv.dataset.state = "active"
                        aKeyDiv.style.backgroundColor = "rgba(0, 255, 0, 0.5)";
                        aKeyDiv.style.border = ".15rem solid rgba(0, 50, 0, 0.75)";
                        aKeyDiv.style.fontWeight = "bold";
                        aKeyDiv.style.transform = "translateY(-.25rem)";
                    }
                    break;
                case "KeyS":
                    if (sKeyDiv.dataset.state == "inactive") {
                        sKeyDiv.dataset.state = "active"
                        sKeyDiv.style.backgroundColor = "rgba(0, 255, 0, 0.5)";
                        sKeyDiv.style.border = ".15rem solid rgba(0, 50, 0, 0.75)";
                        sKeyDiv.style.fontWeight = "bold";
                        sKeyDiv.style.transform = "translateY(-.25rem)";
                    }
                    break;
                case "KeyD":
                    if (dKeyDiv.dataset.state == "inactive") {
                        dKeyDiv.dataset.state = "active"
                        dKeyDiv.style.backgroundColor = "rgba(0, 255, 0, 0.5)";
                        dKeyDiv.style.border = ".15rem solid rgba(0, 50, 0, 0.75)";
                        dKeyDiv.style.fontWeight = "bold";
                        dKeyDiv.style.transform = "translateY(-.25rem)";
                    }
                    break;
            }
        });

        document.addEventListener("keyup", function(event) {
            switch (event.code) {
                case "KeyW":
                    if (wKeyDiv.dataset.state == "active") {
                        wKeyDiv.dataset.state = "inactive"
                        wKeyDiv.style.backgroundColor = "rgba(255, 0, 0, 0.5)";
                        wKeyDiv.style.border = ".15rem solid rgba(255, 0, 0, 0.75)";
                        wKeyDiv.style.fontWeight = "normal";
                        wKeyDiv.style.transform = "translateY(.05rem)";
                    }
                    break;
                case "KeyA":
                    if (aKeyDiv.dataset.state == "active") {
                        aKeyDiv.dataset.state = "inactive"
                        aKeyDiv.style.backgroundColor = "rgba(255, 0, 0, 0.5)";
                        aKeyDiv.style.border = ".15rem solid rgba(255, 0, 0, 0.75)";
                        aKeyDiv.style.fontWeight = "normal";
                        aKeyDiv.style.transform = "translateY(.05rem)";
                    }
                    break;
                case "KeyS":
                    if (sKeyDiv.dataset.state == "active") {
                        sKeyDiv.dataset.state = "inactive"
                        sKeyDiv.style.backgroundColor = "rgba(255, 0, 0, 0.5)";
                        sKeyDiv.style.border = ".15rem solid rgba(255, 0, 0, 0.75)";
                        sKeyDiv.style.fontWeight = "normal";
                        sKeyDiv.style.transform = "translateY(.05rem)";
                    }
                    break;
                case "KeyD":
                    if (dKeyDiv.dataset.state == "active") {
                        dKeyDiv.dataset.state = "inactive"
                        dKeyDiv.style.backgroundColor = "rgba(255, 0, 0, 0.5)";
                        dKeyDiv.style.border = ".15rem solid rgba(255, 0, 0, 0.75)";
                        dKeyDiv.style.fontWeight = "normal";
                        dKeyDiv.style.transform = "translateY(.05rem)";
                    }
                    break;
            }
        });
    }
});
//

// Pause button functionality
document.addEventListener("DOMContentLoaded", function(event) {
    const pauseButton = document.querySelector(".pauseUnpause");
    if (pauseButton) {
        pauseButton.addEventListener('click', function onClick() {
            if(pauseButton.dataset.state == "paused"){
                pauseButton.dataset.state = "playing";
                pauseButton.textContent = "Pause";
            } else {
                pauseButton.dataset.state = "paused";
                pauseButton.textContent = "Play";
            }
        });
    }
});
//

// Return home button functionality
document.addEventListener("DOMContentLoaded", function(event) {
    const returnButton = document.querySelector(".returnButton");
    if (returnButton) {
        returnButton.addEventListener('click', function onClick() {
            if(returnButton.dataset.state == "exploring"){
                returnButton.dataset.state = "returning";
                returnButton.textContent = "Returning to Commander...";
            } else {
                returnButton.dataset.state = "exploring";
                returnButton.textContent = "Return to Commander";
            }
        });
    }
});
//

// Image override button functionality
document.addEventListener("DOMContentLoaded", function(event) {
    const confirmPrediction = document.querySelector(".confirm");
    const rejectPrediction = document.querySelector(".reject");
    const redoPrediction = document.querySelector(".rescan");
    const imageToCheck = document.querySelector(".override");
    imageToCheck.src = imgList[0];
    if (confirmPrediction) {
        confirmPrediction.addEventListener('click', function onClick() {
            if(confirmPrediction.dataset.state == "inactive"){
                confirmPrediction.dataset.state = "active";
                confirmPrediction.textContent = "Confirmed!";
                usedImage = imgList[0];
                imgList.shift();
                imageToCheck.src = "";
                setTimeout(() => {
                    imageToCheck.src = imgList[0];
                    imgList.push(usedImage);
                    confirmPrediction.dataset.state = "inactive";
                    confirmPrediction.textContent = "Confirm";
                }, 1000);
            }
        });
    }
    if (rejectPrediction) {
        rejectPrediction.addEventListener('click', function onClick() {
            if(rejectPrediction.dataset.state == "inactive"){
                rejectPrediction.dataset.state = "active";
                rejectPrediction.textContent = "Rejected!";
                usedImage = imgList[0];
                imgList.shift();
                imageToCheck.src = "";
                setTimeout(() => {
                    imageToCheck.src = imgList[0];
                    imgList.push(usedImage);
                    rejectPrediction.dataset.state = "inactive";
                    rejectPrediction.textContent = "Reject";
                }, 1000);
            }
        });
    }
    if (redoPrediction) {
        redoPrediction.addEventListener('click', function onClick() {
            if(redoPrediction.dataset.state == "inactive"){
                redoPrediction.dataset.state = "active";
                redoPrediction.textContent = "Rescanning!";
                usedImage = imgList[0];
                imgList.shift();
                imageToCheck.src = "";
                setTimeout(() => {
                    imageToCheck.src = imgList[0];
                    imgList.push(usedImage);
                    redoPrediction.dataset.state = "inactive";
                    redoPrediction.textContent = "Rescan";
                }, 1000);
            }
        });
    }
});
//

// Update List tracker and functionality
document.addEventListener("DOMContentLoaded", function(event) {
    const updateList = document.querySelector(".list");
    if (updateList) {
        document.addEventListener('keydown', function(event) {
            switch (event.code) {
                case "Enter":
                var li = document.createElement("li");
                li.appendChild(document.createTextNode(`Update #${document.getElementsByTagName("li").length + 1}`));
                updateList.appendChild(li);
                updateList.scrollTop = updateList.scrollHeight;
            }
        });
    }
});
//
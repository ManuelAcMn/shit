let times = 0
const counterButton = document.querySelector('#Squish');
counterButton.addEventListener('click', (e) => {
    times += 1
    /*let audio = new Audio("sound/kuru1.mp3");
    audio.play();*/
    if (times == 1) {
        document.querySelector('#count').textContent = "She was squished "+times+" time"
    }
    else {
        document.querySelector('#count').textContent = "She was squished "+times+" times"
    }

    /*audio.addEventListener("ended", function () {
        this.remove();
    });*/
});

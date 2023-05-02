function countdown() {
    const eventBox = document.getElementById('event-box')
    const countdownBox = document.getElementById('countdown-box')

    console.log(eventBox.textContent);

    const eventDate = Date.parse(eventBox.textContent)

    console.log(eventDate);

    const myCountdown = setInterval(()=>{

        // Current datetime
        const now = new Date().getTime()

        // Difference between end datetime and current datetime
        const diff = eventDate - now

        // Get difference for the number of days, hours, minutes and seconds 
        const d = Math.floor(eventDate / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24)))
        const h = Math.floor((eventDate / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24)
        const m = Math.floor((eventDate / (1000 * 60) - (now / (1000 * 60))) % 60)
        const s = Math.floor((eventDate / (1000) - (now / (1000))) % 60) 

        countdownBox.innerHTML = d + " days, " + h + " hours, " + m + " minutes, " + s + " seconds"

        // If eventDatetime is ahead of current datetime, once countdown hits 0 will display "Your Time Is Up"
        if (diff > 0) {
            countdownBox.innerHTML = d + " days, " + h + " hours, " + m + " minutes, " + s + " seconds"
        } else {
            clearInterval(myCountdown)
            countdownBox.innerHTML = "Your Time Is Up!"
        }

    }, 1000)

}


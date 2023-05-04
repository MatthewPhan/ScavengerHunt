const title = window.document.title;
const url = window.document.location.href;
const shareButton = document.getElementById('sharebtn');

const shareData = {
    title: `${title}`,
    text: "Congratulations, you have conquered NUS SOC's Scavenger Hunt! #nuscomputing #soclife #classof2027 ",
    url: `${url}`
};

// When button is pressed 
shareButton.addEventListener("click", async () => {
    try {

        // Fetch image
        const response = await fetch("../media/poster/scavenger_hunt_congrats.png");

        // Convert to blob
        const blob = await response.blob();

        // Pass blob into file var 
        const file = new File([blob], "scavenger_hunt_congrats.png", { type: "image/png" });

        // Check if file is supported by user agent (Validating share data), if return true share media file. If false, share URL instead
        if (navigator.canShare({ files: [file] })) {

            //Share Media File
            await navigator.share({
                files: [file],
                title: `${title}`,
                text: "Congratulations, you have conquered NUS SOC's Scavenger Hunt! #nuscomputing #soclife #classof2027 "
            });

            console.log("File shared successfully.");

        } else {

            //Share URL, Text and Title
            await navigator.share(shareData);
            console.log("URL shared successfully.");

        }

    } catch (err) {

        console.log(err);

        if (err.name != "AbortError") {
            // Remove Share Button and Display Main Social Media Icons to share manually without Web Share API
            var x = document.getElementById("socialmedia");
            var shareButton = document.getElementById('sharebtn');

            x.style.display = "block";
            shareButton.style.display = "none";
        } 

    }

});

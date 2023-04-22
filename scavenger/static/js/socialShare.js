const title = window.document.title;
const url = window.document.location.href;
const shareButton = document.getElementById('sharebtn');

const shareData = {
    title: `${title}`,
    text: "Congratulations, you have conquered SOC's scavenger hunt!",
    url: `${url}`
};

// When button is pressed 
shareButton.addEventListener("click", async () => {
    try {

        // Fetch image
        const response = await fetch("../media/poster/congrats.jpeg");

        // Convert to blob
        const blob = await response.blob();

        // Pass blob into file var 
        const file = new File([blob], "congrats.jpeg", { type: "image/jpeg" });

        // Check if file is supported by user agent (Validating share data), if return true share media file. If false, share URL instead
        if (navigator.canShare({ files: [file] })) {

            //Share Media File
            await navigator.share({
                files: [file]
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

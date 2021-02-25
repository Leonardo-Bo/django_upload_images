const feedBackArea = document.querySelector(".invalid_feedback");
    const pErr = document.querySelector(".pErr");
    const submitBtn = document.querySelector("#submit_btn");
    const idImages = document.querySelector("#id_images")

    submitBtn.onclick = function(e) {
        if (idImages.value == "") {
        e.preventDefault();
        feedBackArea.style.display = "block";
        feedBackArea.innerHTML = `<p>No files to upload</p>`;

        setTimeout(function(){
            feedBackArea.style.display = "none";
            }, 2500);

        }
    }
const titleField = document.querySelector("#titleField");
const feedBackArea = document.querySelector(".invalid_feedback");
const titleSuccessOutput = document.querySelector(".titleSuccessOutput");
const submitBtn = document.querySelector(".submit-btn");


titleField.addEventListener("keyup", (e) => {
  const titleVal = e.target.value;

  titleSuccessOutput.style.display = "block";

  titleField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";

  if (titleVal.length === 0) {
    submitBtn.disabled = true;
  }

  if (titleVal.length > 0) {
    fetch("validate-title/", {
      body: JSON.stringify({ title: titleVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        titleSuccessOutput.style.display = "none";
        if (data.title_error) {
          titleField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.title_error}</p>`;
          console.log(data.title_error)
          submitBtn.disabled = true;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});
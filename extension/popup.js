document.addEventListener("DOMContentLoaded", function() {
    chrome.storage.local.get("selectedText", function(data) {
        if (data.selectedText) {
            document.getElementById("selectedText").value = data.selectedText;
        }
    });

    document.getElementById("checkBtn").addEventListener("click", function() {
        let userText = document.getElementById("selectedText").value;
        if (!userText) {
            alert("Please enter text to check.");
            return;
        }

        fetch("http://localhost:8501/fact_check", {  // Change this to your deployed API
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: userText })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = "Result: " + data.fact_check_result;
        })
        .catch(error => {
            document.getElementById("result").innerText = "Error checking misinformation.";
            console.error("Error:", error);
        });
    });
});

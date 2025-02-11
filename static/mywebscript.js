let RunSentimentAnalysis = () => {
    /**
     * Analyzes the sentiment of the text input by the user.
     * Retrieves the text from the input field with ID "textToAnalyze",
     * sends it to the sentiment analysis server, and updates the
     * inner HTML of the element with ID "system_response" based on
     * the server's response.
     *
     * Error Handling:
     * - Displays "The input text is required!" if the input is empty.
     * - Displays "Invalid input ! Try again." for any other errors.
     */
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        } else if (this.status == 400) {
            document.getElementById("system_response").innerHTML = "The input text is required!";
        } else {
            document.getElementById("system_response").innerHTML = "Invalid input ! Try again.";
        }
    };
    xhttp.open("GET", "sentimentAnalyzer?textToAnalyze" + "=" + textToAnalyze, true);
    xhttp.send();
}

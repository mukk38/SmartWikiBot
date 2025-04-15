async function sendQuestion() {
    const input = document.getElementById("question-input");
    const question = input.value.trim();
    if (!question) return;

    // Display user question
    const chatBox = document.getElementById("chat-box");
    const userDiv = document.createElement("div");
    userDiv.className = "message user-message";
    userDiv.innerHTML = `<span>${question}</span>`;
    chatBox.appendChild(userDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send question to backend
    try {
        const response = await fetch("http://localhost:8000/api/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question }),
        });
        const data = await response.json();

        // Display bot response
        const botDiv = document.createElement("div");
        botDiv.className = "message bot-message";
        botDiv.innerHTML = `<span>${data.response}</span>`;
        chatBox.appendChild(botDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        console.error("Error:", error);
        const botDiv = document.createElement("div");
        botDiv.className = "message bot-message";
        botDiv.innerHTML = `<span>Sorry, an error occurred.</span>`;
        chatBox.appendChild(botDiv);
    }

    input.value = "";
}

// Load chat history on page load
async function loadHistory() {
    try {
        const response = await fetch("http://localhost:8000/api/history");
        const history = await response.json();
        const chatBox = document.getElementById("chat-box");
        history.forEach(({ question, response }) => {
            const userDiv = document.createElement("div");
            userDiv.className = "message user-message";
            userDiv.innerHTML = `<span>${question}</span>`;
            chatBox.appendChild(userDiv);

            const botDiv = document.createElement("div");
            botDiv.className = "message bot-message";
            botDiv.innerHTML = `<span>${response}</span>`;
            chatBox.appendChild(botDiv);
        });
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        console.error("Error loading history:", error);
    }
}

window.onload = loadHistory;
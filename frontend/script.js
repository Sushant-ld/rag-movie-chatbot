const questionInput =
    document.getElementById("question");

const sendButton =
    document.getElementById("sendButton");

const chat =
    document.getElementById("chat");


function addMessage(text, type) {

    const message =
        document.createElement("div");

    message.className =
        `message ${type}`;

    const bubble =
        document.createElement("div");

    bubble.className = "bubble";

    bubble.textContent = text;

    message.appendChild(bubble);

    chat.appendChild(message);

    chat.scrollTop = chat.scrollHeight;

    return message;
}


async function sendQuestion() {

    const question =
        questionInput.value.trim();

    if (!question) {

        return;
    }


    // Show user message

    addMessage(
        question,
        "user"
    );


    // Clear input

    questionInput.value = "";


    // Show loading

    const loading =
        addMessage(
            "Thinking...",
            "bot"
        );


    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        question: question
                    })
                }
            );


        const data =
            await response.json();


        // Remove loading message

        loading.remove();


        if (!response.ok) {

            addMessage(
                data.detail ||
                "Something went wrong.",
                "bot"
            );

            return;
        }


        // Add answer

        addMessage(
            data.answer,
            "bot"
        );


        // Add sources

        if (
            data.sources &&
            data.sources.length > 0
        ) {

            const sourceContainer =
                document.createElement("div");

            sourceContainer.className =
                "sources";


            const title =
                document.createElement("strong");

            title.textContent =
                "Sources";

            sourceContainer.appendChild(
                title
            );


            data.sources.forEach(
                source => {

                    const div =
                        document.createElement(
                            "div"
                        );

                    div.className =
                        "source";

                    div.textContent =
                        `${source.title} — ` +
                        `${source.year} · ` +
                        `${source.genre} · ` +
                        `${source.director}`;

                    sourceContainer.appendChild(
                        div
                    );

                }
            );


            chat.appendChild(
                sourceContainer
            );

            chat.scrollTop =
                chat.scrollHeight;
        }


    } catch (error) {

        loading.remove();

        addMessage(
            "Could not connect to the API. " +
            "Make sure FastAPI is running.",
            "bot"
        );

        console.error(error);
    }
}


sendButton.addEventListener(
    "click",
    sendQuestion
);


questionInput.addEventListener(
    "keydown",
    event => {

        if (event.key === "Enter") {

            sendQuestion();

        }

    }
);
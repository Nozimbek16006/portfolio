document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("a");
    links.forEach(link => {
        link.addEventListener("click", () => {
            document.body.classList.add("navigating");
        });
    });
});


function toggleReply(button, replyId) {
    const reply = document.getElementById(replyId);

    if (!reply) return;

    const opening = reply.hidden;

    reply.hidden = !opening;
    button.setAttribute("aria-expanded", String(opening));

    const label = button.querySelector(".reply-button-text");

    if (label) {
        label.textContent = opening
            ? "Javoblarni yashirish"
            : "Javoblar";
    }
}

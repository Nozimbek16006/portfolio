document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("a");
    links.forEach(link => {
        link.addEventListener("click", () => {
            document.body.classList.add("navigating");
        });
    });
});

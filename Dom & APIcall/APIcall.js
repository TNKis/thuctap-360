function updateDOM() {
    const element = document.getElementById("demo");
    if (element) {
        element.innerHTML = "Nội dung đã được cập nhật!";
        element.style.color = "blue";
    }
}
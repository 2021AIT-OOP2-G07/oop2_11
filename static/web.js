document.querySelector("#uploadBtn").addEventListener("click", (e) => {
    e.preventDefault()
    document.getElementById("uploadArea").style.display = "block"
    document.getElementById("uploadListArea").style.display = "none"
    document.getElementById("glayscaleArea").style.display = "none"

    // 
});

document.querySelector("#uploadListBtn").addEventListener("click", (e) => {
    e.preventDefault()
    document.getElementById("uploadArea").style.display = "none"
    document.getElementById("uploadListArea").style.display = "block"
    document.getElementById("glayscaleArea").style.display = "none"

    // ここにアップロードリストを表示するやつ
});

document.querySelector("#grayscaleBtn").addEventListener("click", (e) => {
    e.preventDefault()
    document.getElementById("uploadArea").style.display = "none"
    document.getElementById("uploadListArea").style.display = "none"
    document.getElementById("grayscaleArea").style.display = "block"

    // ここにグレースケールを表示するやつ
});

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

    // ここにアップロード\リストを表示するやつ
    fetch("/upload")(response => {
        response.then((data) => {
            const tableBody = document.querySelector("#uploadListArea > div");
            tableBody.innerHTML = ""
            data.forEach(elm => {                
                let img = document.createElement('img');
                tableBody.appendChild(img);

            });    
        })
    })
})

document.querySelector("#grayscaleBtn").addEventListener("click", (e) => {
    e.preventDefault()
    document.getElementById("uploadArea").style.display = "none"
    document.getElementById("uploadListArea").style.display = "none"
    document.getElementById("grayscaleArea").style.display = "block"

    // ここにグレースケールを表示するやつ
    fetch("/greyscale")(response => {
        response.then((data) => {
            const tableBody = document.querySelector("#grayscaleArea > div");
            tableBody.innerHTML = ""
            data.forEach(elm => {                
                let img = document.createElement('img');
                tableBody.appendChild(img);

            });    
        })
    })
});

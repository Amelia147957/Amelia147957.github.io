const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";

fetch(url)
    .then(response => response.json())
    .then(data => {
        const results = data["data"]["results"];
        let attractionsList = []; //景點+圖片

        results.forEach(result => {
            const title = result["stitle"];
            const imgUrls = result["filelist"].match(/https:\/\/.*?\.(jpg|jpeg|png|gif)/gi);
            const firstImageUrl = imgUrls && imgUrls.length > 0 ? imgUrls[0] : 'placeholder.jpg';

            attractionsList.push({
                name: title,
                imageUrl: firstImageUrl
            });
        });

        updateContent(attractionsList);
        //console.log("Attractions list:", attractionsList);
    })
    .catch(error => {
        console.error('Error:', error);
    });

function updateContent(attractionsList) {
    //前面有遇到像素不同景點也不同的問題，所以解決辦法在這裡
    const desktopBoxes = document.querySelectorAll(".desktop .small_box, .desktop .pic_big, .desktop .pic_small");
    const ipadBoxes = document.querySelectorAll(".ipad .small_box, .ipad .pic_big, .ipad .pic_small");
    const mobileBoxes = document.querySelectorAll(".mobile .small_box, .mobile .pic_big, .mobile .pic_small");

    // 更新桌面版
    updateBoxes(desktopBoxes, attractionsList);
    // 更新iPad版
    updateBoxes(ipadBoxes, attractionsList);
    // 更新手機版
    updateBoxes(mobileBoxes, attractionsList);
}

function updateBoxes(boxes, attractionsList) {
    attractionsList.forEach((attraction, index) => {
        if (index < boxes.length) {
            const box = boxes[index];

            //標題
            const title = document.createElement('h2');
            title.textContent = attraction.name;

            //圖片
            const image = document.createElement('img');
            image.src = attraction.imageUrl;
            image.alt = 'Image of ' + attraction.name;
            image.style.width = "100%";
            image.style.height = "auto";


            //p段落
            const text = document.createElement('p');
            text.textContent = attraction.name;


            //更新 box 內容
            box.appendChild(image);
            box.appendChild(title);
            box.appendChild(text);
        }
    });
}


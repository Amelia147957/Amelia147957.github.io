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
            const image = box.querySelector('img');
            const title = box.querySelector('h2');
            const text = box.querySelector('.text p');

            image.src = attraction.imageUrl;
            image.alt = 'Image of ' + attraction.name;

            // 如果有 title 和 text 的話，更新文字內容(因為small_box跟pic_big、pic_small裡面內容不太一樣)
            if (title) {
                title.textContent = attraction.name;
            }
            if (text) {
                text.textContent = attraction.name;
            }
        }
    });
}

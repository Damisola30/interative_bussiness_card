function updateCard() {
    // Get the input values
    const name = document.getElementById('name').value;
    const img = document.getElementById('imageUpload').files[0];
    const title = document.getElementById('title').value;
    const email = document.getElementById('email').value;
    const about = document.getElementById('about').value;
    const interest = document.getElementById('interest').value;

    // Update the business card with input values
    document.getElementById('cardName').textContent = name || 'Your Name';
    if (img) {
    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('cardImage').src = e.target.result;
    };
    reader.readAsDataURL(img);
    } else {
        // Default image remains if no image is uploaded
        document.getElementById('cardImage').src = defaultimg_url;
    }
    document.getElementById('cardTitle').textContent = title || 'Your Job';
    // document.getElementById('cardEmail').textContent = email || 'youremail@example.com';
    document.getElementById('cardAbout').textContent = about || 'About you';
    document.getElementById('cardInterest').textContent = interest || 'Your interests';
}
function test(){
    console.log("testingg")
}

function downloadCard() {
    console.log("Attempting to capture business card...")
 
    html2canvas(document.getElementById('business-card')).then(function(canvas) {
        console.log("Canvas created, preparing download...");
        let filename = document.getElementById('name').value || 'bussiness-card'
        // Convert canvas to a data URL and create a download link
        let link = document.createElement('a');
        link.download = `${filename}.png`
        link.href = canvas.toDataURL("image/png");
        link.click();
        console.log("Download triggered.");
    }).catch(function(error) {
        console.error("Error capturing the card:", error);
    });
   
   
}
test()


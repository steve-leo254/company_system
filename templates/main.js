// JavaScript code to handle the video stream and barcode detection

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

// Constraints for the video stream (using the default camera)
const constraints = { video: { facingMode: 'environment' } };

// Function to start the video stream
async function startVideo() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        video.srcObject = stream;
    } catch (err) {
        console.error('Error accessing the camera:', err);
    }
}

// Function to handle the barcode detection
function detectBarcode() {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    const detectedBarcode = decode(imageData.data, canvas.width, canvas.height);

    if (!detectedBarcode || detectedBarcode.length === 0) {
        console.log('No Barcode Detected');
    } else {
        for (const barcode of detectedBarcode) {
            if (barcode.data) {
                console.log('Barcode Data:', barcode.data);
                break;
            }
        }
    }

    requestAnimationFrame(detectBarcode);
}

// Start the video stream and barcode detection
startVideo();
video.addEventListener('play', detectBarcode);

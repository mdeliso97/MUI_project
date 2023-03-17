const canvasElement = document.getElementsByClassName('output_canvas')[0];
const canvasCtx = canvasElement.getContext('2d');
const videoElement = document.getElementsByClassName('input_video')[0];

function sendFrame() {
    canvasCtx.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);
    const imageData = canvasCtx.getImageData(0, 0, canvasElement.width, canvasElement.height);
    ws.send(imageData.data);
}
setInterval(sendFrame, 16);

ws.addEventListener('message', (event) => {
    const poseData = JSON.parse(event.data);
    const poseLandmarks = poseData.pose_landmarks;

    // Draw pose landmarks on the canvas element
    canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
    drawConnectors(canvasCtx, poseLandmarks, POSE_CONNECTIONS,
        {color: '#00FF00', lineWidth: 4});
    drawLandmarks(canvasCtx, poseLandmarks,
        {color: '#FF0000', lineWidth: 2});
});

function updateClock() {

    const now = new Date();
    
    const seconds = now.getSeconds();
    const minutes = now.getMinutes();
    const hours   = now.getHours();

    const secondDeg = ((seconds / 60) * 360);
    const minuteDeg = ((minutes / 60) * 360) + ((seconds/60)*6);
    const hourDeg   = ((hours / 12) * 360) + ((minutes/60)*30);

    document.getElementById('second-hand').style.transform = `translateX(-50%) rotate(${secondDeg}deg)`;
    document.getElementById('minute-hand').style.transform = `translateX(-50%) rotate(${minuteDeg}deg)`;
    document.getElementById('hour-hand').style.transform = `translateX(-50%) rotate(${hourDeg}deg)`;
}

function runClock() {
    updateClock();
    requestAnimationFrame(runClock);
}

runClock();

// Alternate method
// setInterval(updateClock, 1000);
// updateClock();
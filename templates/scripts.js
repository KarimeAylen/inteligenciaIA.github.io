var video = document.getElementById('video');

        // Función para iniciar la cámara
        function startCamera() {
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({ video: true })
                    .then(function (stream) {
                        video.srcObject = stream;
                    })
                    .catch(function (error) {
                        console.log("Error al acceder a la cámara: " + error);
                    });
            } else {
                console.log("La cámara no está disponible en este dispositivo.");
            }
        }

        // Función para detener la cámara
        function stopCamera() {
            if (video.srcObject) {
                video.srcObject.getTracks().forEach(function (track) {
                    track.stop();
                });
                video.srcObject = null;
            }
        }

        // Evento click para iniciar la cámara
        var startButton = document.getElementById('startButton');
        startButton.addEventListener('click', startCamera);

        // Evento click para detener la cámara
        var stopButton = document.getElementById('stopButton');
        stopButton.addEventListener('click', stopCamera);
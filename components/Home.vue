<template>
  <div>
    <!-- content start -->
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>MQTT IP Display</title>
      <link rel="stylesheet" href="assets/css/style.css">
    </head>

    <body>
      <div class="validateBox">
        <a href="https://strathmore.edu/" target="_blank"><img src="/images/strathmore university-transperent.png"></a>
        <h2>Savanna Trace<br>LoRaWAN Gateway</h2>
        <form>
          <textarea placeholder="IP address details" id="textarea1" class="input"></textarea>
          <br><br>
          <button onclick="executePythonScript">Request IP Address</button><br><br>

          <button><a href="/SavannaTraceApp/savanna1.py" download="savanna1.py" target="_blank">
                    Download IP Data
                </a>
            </button> 

         
        </form>
      </div>

      <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
      <script>
        new Vue({
          el: '.validateBox',
          methods: {
            executePythonScript() {
              fetch('localhost:3000/SavannaTraceApp/savanna1.py') 
                .then(response => response.text())
                .then(data => {
                  const textareaElement = document.getElementById('textarea1');
                  textareaElement.value = data || 'No data received.';
                })
                .catch(error => {
                  console.error('Error fetching data:', error);
                });
            }
          }
        });
      </script>
    </body>
    <!-- body content ends -->
  </div>
</template>

<style scoped> 
/* CSS styles */
body {
  /* background: rgba(255, 255, 255, 0.5); */
  background: url("/images/strathmore-uni2.png");
  background-size: cover;
  background-repeat:inherit;
  width: 100%;
  height: 100%;
  margin: 0 auto;
  margin-top: 10px;
  margin-bottom: 100px;
}

.validateBox {
  background-color: whitesmoke;
  opacity: 0.85;
  padding: 40px;
  width: 80%; /* Adjustable width */
  max-width: 400px; /* maximum width for larger screens */
  margin: 90px auto; /* Box centered horizontally */
  border-radius: 10px;
  text-align: center;
  position: relative;
  z-index: 1;
}

form {
  width: 100%;
  text-align: center;
  margin-top: -10;
}

input {
  width: 100%;
  text-align: center;
  background: transparent;
  border: none;
  border-bottom: 2px solid white;
  font-size: 18px;
  font-weight: 200px;
  padding: 10px 0;
  transition: border 0.5s;
  outline: none;
  height: 35px;
  color: rgb(37, 36, 36);
}

button {
  border: none;
  width: 75%;
  font-size: 20px;
  line-height: 25px;
  padding: 10px;
  border-radius: 25px;
  background-color: rgb(110, 27, 27);
  color: white;
  cursor: pointer;
}

button:hover {
  background:#a34f00;
  color: white;
}

.validateBox h2 {
  color: rgb(110, 27, 27);
  font-family: sans-serif;
}

.validateBox textarea {
  font-family: sans-serif;
  width: 75%;
}

::placeholder {
  color: grey;
  text-align: center;
  opacity: 0.8;
}

/* Media Query for Mobile */
@media (max-width: 600px) {
  .validateBox {
    width: 75%;
    margin: 40px auto;
  }
}

/* Media Query for Desktop and Larger Screens */
@media (min-width: 601px) {
  .validateBox {
    width: 40%;
  }
}
</style>

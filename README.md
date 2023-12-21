This project contains an application that uses MQTT to request an IP address
 The python application can:
 1. Connect to the MQTT broker. if it fails it retries after a set time say 5 seconds
 until it connects.
 2. Read the IP address assigned from WIFI
 3. Send the IP address to a user subscribing to the same topic
 As a bonus, this project has a user interface with Nuxt VUEJS that would show prompts and displays the IP address
 when a button is clicked.

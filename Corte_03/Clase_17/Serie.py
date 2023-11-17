#comunicacion serial rs232
#uso de libreria
#-m pip install pyserial 
#uso de la libreria pyserial
# para instalar ejecutar -m pip install pyserial
import serial
import time

puerto=serial.Serial('COM1',baudrate=9600,timeout=1)
lista=[]
while 1:
    dato=input('Dato a enviar: ')
    for i in range (3):
        puerto.write(dato.encode('utf-8'))
        line=puerto.readline().decode('ascii')
        time.sleep(0.3)
        #print(str(line).rstrip('\r\n'))
        if str(line).rstrip('\r\n')=='Dato incorrecto':
            print('Error en los datos')
            break
        lista.append(str(line).rstrip('\r\n'))
    print(lista)
    lista=[]

'''
//--------Codigo de Arduino---------
long randomNumber;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  digitalWrite(LED_BUILTIN, LOW);
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available() > 0) {
    char incoming = Serial.read();
    if (incoming == 'y') {
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      randomNumber=random(0,100);
      Serial.println(randomNumber);
      delay(200);                       // wait for a second
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
      delay(200);                       // wait for a second
    }else{
      Serial.println("Dato incorrecto");
    }
  }
}'''
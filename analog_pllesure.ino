// These constants won't change. They're used to give names to the pins used:
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
#define yellow 8

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)
int ave_pressure = 0;
int sum_pressure = 0;
void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
   for (int i = 0; i < 10; i++)
  {
    sensorValue = analogRead(analogInPin);
    sum_pressure += sensorValue;
  }
  ave_pressure = sum_pressure / 10;
  Serial.println("average");
  Serial.println(ave_pressure);
  pinMode(yellow, OUTPUT);
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);
  // map it to the range of the analog out:
  outputValue = map(sensorValue, 0, 1023, 0, 1500);
  // print the results to the Serial Monitor:
  if(sensorValue - ave_pressure >= 2)
  {
    Serial.println("true\n\n\n\n\n\n\n"); 
    digitalWrite(yellow, HIGH);
    delay(2000);
  }
  
  Serial.println("sensor = ");
  Serial.println(sensorValue);
  
  /*Serial.print("\t output = ");
  Serial.println(outputValue);*/
  // wait 2 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
  delay(100);
  digitalWrite(yellow, LOW);
}

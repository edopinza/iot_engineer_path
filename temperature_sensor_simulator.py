import random
from datetime import datetime
import json


class SmartSensor:
    def __init__(self, upper_limit: float, lower_limit: float) -> None:
        self._upper_limit = upper_limit
        self._lower_limit = lower_limit
        self.records = []
        self.current_temperature = None
        self.current_time = None

    def record_temperature(self):
        # Registra una temperatura associata al timestamp. Il valore è generato randomicamente.
        self.current_time = datetime.now().timestamp()
        self.current_temperature = round(random.uniform(36.5, 37.5), 2)

        if len(self.records) > 10:
            del self.records[0]

        self.records.append({self.current_time: self.current_temperature})

    def alert(self):
        # Stampa su terminale un alert se la temperatura va oltre il limite minimo o massimo
        if self.current_temperature < self._lower_limit:
            print("WARNING: temperature is too low!")
        elif self.current_temperature > self._upper_limit:
            print("WARNING: temperature is too high!")

    def get_json_payload(self):
        # Converte 
        payload_dict = {
            "timestamp": list(self.records[0].keys())[0],
            "temperature": list(self.records[0].values())[0],
        }

        del self.records[0]

        return json.dumps(payload_dict)


incubator_sensor = SmartSensor(upper_limit=37.2, lower_limit=36.8)
incubator_sensor.record_temperature()
incubator_sensor.alert()

payload = incubator_sensor.get_json_payload()
print(f"Payload pronto per la rete: {payload}")
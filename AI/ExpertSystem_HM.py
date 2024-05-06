class ExpertSystem:
    def __init__(self):
        self.rules = {
            "cold": {
                "symptoms": ["sneezing", "cough", "runny nose"],
                "diagnosis": "common cold"
            },
            "flu": {
                "symptoms": ["fever", "body aches", "fatigue"],
                "diagnosis": "influenza"
            },
            "allergy": {
                "symptoms": ["itchy eyes", "sneezing", "rash"],
                "diagnosis": "allergic reaction"
            }
        }

    def get_diagnosis(self, symptoms):
        for illness, data in self.rules.items():
            if all(symptom in symptoms for symptom in data["symptoms"]):
                return data["diagnosis"]
        return "unknown"
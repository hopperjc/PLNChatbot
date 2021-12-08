# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionGetAppointment(Action):
    def name(self):
        return 'action_appointment'

    def run(self, dispatcher, tracker, domain):
        spt = tracker.get_slot('specialty')
        time = tracker.get_slot('time')
        day = tracker.get_slot('day')

        global appointments

        appointments = result(spt, time, day)
        appointments.drop_duplicates(inplace=True)

        response = str(row["specialty"] )

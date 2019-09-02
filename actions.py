from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import Restarte
from rasa_sdk.events import SlotSet

import requests
import json


class action_get_weather(Action):
    def name(self) -> Text:
        return 'action_get_weather'

    def run(dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hello World!")

class action_save_cust_info(Action):
    def name(self) -> Text:
        return 'action_save_cust_info'

    def run(dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_id = (tracker.current_state())["sender_id"]
        cust_name = next(tracker.get_latest_entity_values("cust_name"), None)
        cust_sex = next(tracker.get_latest_entity_values("cust_sex"), None)
        bot_position = "Mình"
        dispatcher.utter_message("here's what I found:")
        if (cust_sex is  None):
            cust_sex = "Quý khách"

        if (cust_sex == "anh") | (cust_sex == "chị"):
           bot_position = "em"
        elif (cust_sex == "cô") | (cust_sex == "chú"):
            bot_position = "cháu"
        else:
            cust_sex = "bạn"
            bot_position = "mình"

        if not cust_name:
            #dispatcher.utter_template("utter_greet_name",tracker)
            return []
        
        return [SlotSet('cust_name', cust_name),SlotSet('cust_sex', cust_sex ),SlotSet('bot_position', bot_position)]

class action_save_mobile_no(Action):
    def name(self) -> Text:
        return 'action_save_mobile_no'

    def run(dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_id = (tracker.current_state())["sender_id"]
        mobile_no = next(tracker.get_latest_entity_values("inp_number"), None)

        if not mobile_no:
            return  [UserUtteranceReverted()]

        mobile_no = mobile_no.replace(" ","")
        #print (cust_name)
        return [SlotSet('mobile_no', mobile_no)]


class action_reset_slot(Action):

    def name(self) -> Text:
        return "action_reset_slot"

    def run(dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("transfer_nick", None),SlotSet("transfer_amount", None),SlotSet("transfer_amount_unit", None)]


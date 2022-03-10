from events.base_event import BaseEvent
from assets import lib
from datetime import datetime


# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class
class UpdateStuff(BaseEvent):

    def __init__(self):
        interval_minutes = 60  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    async def run(self, client):
        day = datetime.today().weekday()
        hour = datetime.now().hour
        if hour == 2:
          lib.UpdateExcel()
          
        if day == 6 and hour == 5:
            lib.UpdateExcel()
            msg = "#events 7"
            await client.get_channel(893625759292330064).send(":regional_indicator_h: :regional_indicator_a: :regional_indicator_v: :regional_indicator_e:  :regional_indicator_a:  :regional_indicator_g: :regional_indicator_r: :regional_indicator_e: :regional_indicator_a: :regional_indicator_t:  :regional_indicator_w: :regional_indicator_e: :regional_indicator_e: :regional_indicator_k: :exclamation:")
            await client.get_channel(893625759292330064).send(msg)
            



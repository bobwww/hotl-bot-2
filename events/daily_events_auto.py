from events.base_event import BaseEvent
from assets import lib
from datetime import datetime


# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class
class UpdateStuff(BaseEvent):

    def __init__(self):
        interval_minutes = 1 # 1440 - 24h # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    async def run(self, client):
        hour = datetime.now().hour
        min = datetime.now().minute
        day = datetime.today().weekday()

        if(day == 4):
          if hour == 5 and min == 0:
            msg = lib.DailyChanges()
            await client.get_channel(893625759292330064).send(msg)
          if  hour == 15 and min == 0:
            await client.get_channel(893625759292330064).send(":regional_indicator_s: :regional_indicator_h: :regional_indicator_a: :regional_indicator_b: :regional_indicator_a: :regional_indicator_t:  :regional_indicator_s: :regional_indicator_h: :regional_indicator_a: :regional_indicator_l: :regional_indicator_o: :regional_indicator_m:")
        
        #send a messege every saturday 21:00
        if day == 5 and hour == 15 and min == 0:
          msg = lib.DailyChanges()
          await client.get_channel(893625759292330064).send(msg)
          
        if (hour == 13 and min  == 0 and day != 5 and day != 4) or (hour == 5 and min == 0 and day != 5 and day != 4) or (hour == 15 and min  == 0 and day != 5 and day != 4):
          msg = lib.DailyChanges()
          await client.get_channel(893625759292330064).send(msg)



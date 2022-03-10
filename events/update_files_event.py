from events.base_event import BaseEvent
from assets import lib


# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class
class UpdateStuff(BaseEvent):

    def __init__(self):
        interval_minutes = 1440  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    async def run(self, client):
        lib.UpdateExcel()


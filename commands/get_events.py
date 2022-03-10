from commands.base_command import BaseCommand
from assets import lib


class Events(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Get events for X days"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["number of days"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        try:
          lib.UpdateExcel()
          data = lib.GetXEvents(int(params[0]))
          for day in data:
              if type(day) == str:
                  await message.channel.send(day)
              else:
                  date_str = day['תאריך'].strftime("%d-%m-%Y")  # turn Timestamp type into string
                  msg = f"({date_str}) events are:\n"
                  if day["יב'1"] != "No events":
                      msg += '\tGeneral: {0}\n'.format(day["יב'1"])
                  if day["יב'3"] != "No events":
                      msg += '\tMofet: {0}\n'.format(day["יב'3"])
                  if day['הערות'] != "No events":
                      msg += f"\tExtra: {day['הערות']}\n"
                  await message.channel.send("**"+msg+"**")
        except Exception:
            await message.channel.send("Please, provide a valid number of days")
            return
        


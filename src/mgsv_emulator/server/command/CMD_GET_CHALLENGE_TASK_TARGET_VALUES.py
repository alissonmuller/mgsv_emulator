from command.Command import Command

class CMD_GET_CHALLENGE_TASK_TARGET_VALUES(Command):

    def execute(self, data):
        return self._receiver.action(data)

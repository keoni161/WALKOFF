import time

from apps import App, action
from tests.testapps.HelloWorld.exceptions import CustomException


@action
def global1(arg1):
    return arg1


class Main(App):
    def __init__(self, name=None, device=None):
        App.__init__(self, name, device)
        self.introMessage = {"message": "HELLO WORLD"}

    @action
    def helloWorld(self):
        return self.introMessage

    @action
    def repeatBackToMe(self, call):
        return "REPEATING: " + call

    @action
    def returnPlusOne(self, number):
        return number + 1

    @action
    def pause(self, seconds):
        time.sleep(seconds)

    @action
    def addThree(self, num1, num2, num3):
        return num1 + num2 + num3

    @action
    def buggy_action(self):
        raise CustomException

    @action
    def json_sample(self, json_in):
        return (json_in['a'] + json_in['b']['a'] + json_in['b']['b'] + sum(json_in['c']) +
                sum([x['b'] for x in json_in['d']]))

    @action
    def wait_for_pause_and_resume(self):
        import walkoff.case.database as case_database
        from walkoff.case.database import Event
        from walkoff.executiondb.workflowresults import WorkflowStatus
        from walkoff import executiondb

        workflow_status = executiondb.execution_db.session.query(WorkflowStatus).first()

        workflow_id = str(workflow_status.workflow_id)

        events = case_database.case_db.session.query(Event).filter_by(originator=workflow_id).all()

        pause = False
        resume = False
        for event in events:
            if event.message == 'Workflow paused':
                pause = True
            elif event.message == 'Workflow resumed':
                resume = True

        if pause and resume:
            return "success"

        time.sleep(0.1)
        return "failure"

    def shutdown(self):
        return

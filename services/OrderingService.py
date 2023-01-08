from statemachine import StateMachine, State


class OrderingMachine(StateMachine):
    prospect = State('Prospect', initial=True)
    existing = State('Existing')
    registered = State('Registered')
    processing = State('Processing')
    completed = State('Completed', final=True)
    cancelled = State('Cancelled', final=True)

    create_order = prospect.to.existing()
    validate = existing.to.registered()
    process = registered.to.processing()
    complete = processing.to.completed()
    cancel = cancelled.from_(prospect, existing, registered, processing)

    def on_create_order(self):
        pass

    def on_validate(self):
        pass

    def on_process(self):
        pass

    def on_complete(self):
        pass

    def on_cancel(self):
        pass

import json

from example.controller.cli_controller import OneController


def lambda_handler(event, context):
    """
    Example Lambda Handler
    :param event:
    :param context:
    :return:
    """
    event_body = json.loads(event.get("body", "{}"))
    OneController().do_stuff(event_body.get("name", "No Name Passed"), event_body.get("count", 1), context)

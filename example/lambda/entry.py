from example.controller.cli_controller import OneController


def lambda_handler(event, context):
    """
    Example Lambda Handler
    :param event:
    :param context:
    :return:
    """
    OneController().do_stuff(event.get("name", "no-name"), context)

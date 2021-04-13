from hypergrowth.framework import Component


class TwoController(Component):

    def do_other_stuff(self, context):
        """
        matches the interface defined in example_shared.interface_two.do_other_stuff
        :param context: required to handle execution context; similar to when executed via lambda
        :return:
        """
        print(f"doing other stuff")
        print(context)

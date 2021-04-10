from hypergrowth.framework import Component


class OneController(Component):

    def do_stuff(self, name, count, context):
        """
        :param name: matches the interface defined in example_shared.interface_one.do_stuff
        :param count: matches the interface defined in example_shared.interface_one.do_stuff
        :param context: LambdaContext passed in so that we can handle lambda context concern as well
        :return:
        """
        print(f"doing it {name} {count}")
        print(context)


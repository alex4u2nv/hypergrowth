from hypergrowth.framework import Component


class OneController(Component):

    def do_stuff(self, name, count):
        print(f"doing it {name} {count}")

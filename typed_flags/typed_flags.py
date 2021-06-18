from discord.ext import commands
from discord.ext.commands.view import StringView


class TypedFlags(commands.Converter):
    def __init__(self, *, delim=None, start=None):
        self.delim = delim or ":="
        self.start = start or "--"

    async def convert(self, ctx, argument):
        x = True
        argless = []
        data = {"argless": []}
        argument = argument.split(self.start)

        if (length := len(argument)) == 1:
            # No flags
            argless.append(argument[0])
            x = False  # Don't loop

        i = 0
        while x:
            if i >= length:
                # Have consumed all
                break

            if self.delim in argument[i]:
                # Get the arg name minus start state
                arg = argument[i].split(self.delim, 1)

                if len(arg) == 1:
                    # Arg has no value, so its argless
                    # This still removes the start and delim however
                    argless.append(arg)
                    i += 1
                    continue

                arg_name = arg[0]
                arg_value = arg[1].strip()
                view = StringView(arg_value)

                # Get the first matching string
                data[arg_name] = view.get_quoted_word()
                view.skip_ws()

                # The rest is just argless stuff
                while not view.eof:
                    word = view.get_quoted_word()
                    argless.append(word)
                    view.skip_ws()

            else:
                argless.append(argument[i])

            i += 1

        # Time to manipulate argless
        # into the same expected string pattern
        # as dpy's argparsing
        for arg in argless:
            view = StringView(arg)
            while not view.eof:
                word = view.get_quoted_word()
                data["argless"].append(word)
                view.skip_ws()

        if not bool(data["argless"]):
            data.pop("argless")

        return data

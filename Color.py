import os


class TerminalColors:
    """
    This class provides a set of methods for formatting text with ANSI escape codes for terminal colors.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def color(cls, text, color_code):
        """
        Format the given text with the specified color code.

        :param text: the text to format
        :param color_code: the ANSI escape code for the desired color
        :return: the formatted text string
        """
        return f"{color_code}{text}{cls.ENDC}"

    @classmethod
    def header(cls, text):
        """
        Format the given text with the header color.

        :param text: the text to format
        :return: the formatted text string
        """
        return cls.color(text, cls.HEADER)

    @classmethod
    def okblue(cls, text):
        """
        Format the given text with the OK blue color.

        :param text: the text to format
        :return: the formatted text string
        """
        return cls.color(text, cls.OKBLUE)

    @classmethod
    def verbose(cls, text):
        """
        Format the given text with the OK blue color.
        same as OK blue but for easier reading of the code

        :param text: the text to format
        :return: the formatted text string
        """
        return cls.color(text, cls.OKBLUE)

    @classmethod
    def okcyan(cls, text):
        """
        Format the given text with the OK cyan color.

        :param text: the text to format
        :return: the formatted text string
        """
        return cls.color(text, cls.OKCYAN)

    @classmethod
    def okgreen(cls, text):
        """
        Format the given text with the OK green color.

        :param text: the text to format
        :return: the formatted text string
        """
        return cls.color(text, cls.OKGREEN)

    @classmethod
    def warning(cls, text):
        """
        Format the given text with the warning color.

        :param text: the text to format
        :return: the formatted text string
        """
        return cls.color(text, cls.WARNING)

    @classmethod
    def fail(cls, text):
        """
        Format the given text with the fail color.

        :param text: the text to format
        :return: the formatted text string
        """
        return cls.color(text, cls.FAIL)

    @classmethod
    def bold(cls, text):
        """
        Format the given text with bold text.

        :param text: the text to format
        :return: the formatted text string
        """
        return cls.color(text, cls.BOLD)

    @classmethod
    def underline(cls, text):
        """
        Format the given text with underlined text.

        :param text: the text to format
        :return: the formatted text string
        """
        return cls.color(text, cls.UNDERLINE)

    def __repr__(self):
        """
        :param self:
        :return: an array of all the variables
        """
        params: list = []
        for i in vars(TerminalColors):
            params.append(i)
        return params

    def test(self):
        """
        :param self
        :return: zero
        """
        logo: str = """
        ███████╗███╗   ███╗ ██████╗ ██╗     
        ██╔════╝████╗ ████║██╔═══██╗██║     
        ███████╗██╔████╔██║██║   ██║██║     
        ╚════██║██║╚██╔╝██║██║   ██║██║     
        ███████║██║ ╚═╝ ██║╚██████╔╝███████╗
        ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝        
        """
        try:
            print('HEADER\n', self.header(logo), 'OKBLUE\n', self.okblue(logo), 'OKCYAN\n', self.okcyan(logo),
                  'OKGREEN\n',
                  self.okgreen(logo),
                  'WARNING\n', self.warning(logo), 'FAIL\n', self.fail(logo), 'BOLD\n',
                  self.bold(logo),
                  'UNDERLINE\n', self.underline(logo))
            return True
        except Exception as e:
            return e


if __name__ == "__main__":
    os.system('color')
    tc = TerminalColors()
    print(tc.test())

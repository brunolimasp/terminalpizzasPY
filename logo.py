import os
from colour_text import ColourText


class Logo():
    def logo(self):
        os.system("cls")
        ct = ColourText()
        ct.initTerminal()
        print( ct.convert( "The next section is in green: <>green example<>." ) )
        print("\n\n\n\t\t\t\t    1.0 B",)
        print("\t\t\t\tVERSAO PYTHON")
        print(ct.convert("\n\t<>green ######## ######## ########  ##     ## #### ##    ##    ###    ##<>\n"))
        print(ct.convert("\t<>green   ##    ##       ##     ## ###   ###  ##  ###   ##   ## ##   ##<>\n"))
        print(ct.convert("\t<>green   ##    ##       ##     ## #### ####  ##  ####  ##  ##   ##  ##<>\n"))
        print(ct.convert("\t<>green   ##    ######   ########  ## ### ##  ##  ## ## ## ##     ## ##<>\n"))
        print(ct.convert("\t<>green   ##    ##       ##   ##   ##     ##  ##  ##  #### ######### ##<>\n"))
        print(ct.convert("\t<>green   ##    ##       ##    ##  ##     ##  ##  ##   ### ##     ## ##<>\n"))
        print(ct.convert("\t<>green   ##    ######## ##     ## ##     ## #### ##    ## ##     ## ########<>\n\n"))
        print(ct.convert("\t<>green >PIZZAS_<>\n\n\n"))


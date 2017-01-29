class LicenseHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'r')

    def readline(self):
        return self.file.readline()

    def read(self, size):
        return self.file.read(size)

    # Only works for Apache 2.0, super basic method.
    def getDefinitions(self):
        definitions = []
        inDef = False
        for line in self.file:
            l = line.lower().replace(" ","")

            if "3" in l:
                inDef = False

            if inDef:
                definitions.append(line)

            if "definitions" in l:
                inDef = True

        return filter(lambda item: item != '\n', definitions)

    #  Doesn't do anything at the moment, as some text files have no clear sections,
    # so I do not know what comes next after the definitions paragraph to stop.
    # I will make the assumption that sections are numbered, and increment by one, also the section number is always an integer
    def getDefinitionsParagraph(self):
        defParagraphLines = [];

        paragraphNumber = 0
        inDef = False
        # Go through all the lines before the definitions paragraph.
        for line in self.file:
            if "definitions" in line.lower():
                explodedLine = line.lower().replace(".", "").replace("\n", "").split(" ") # Getting rid of random "." and "\n", will make it easier to get the section number.
                defWordIndex = explodedLine.index("definitions")
                trailer = explodedLine[0:defWordIndex]
                paragraphNumber = int(trailer[0])
                inDef = True
                print inDef
                break

        for line in self.file:
            if inDef:
                explodedLine = line.lower().replace(".", "").replace("\n", "").split(" ")
                if explodedLine[0] == str(paragraphNumber + 1):
                    inDef = False
                else:
                    #print line
                    defParagraphLines.append(line);


        return defParagraphLines

    #  If the document provided includes HTML tags, those might prove useful as
    # paragraph headings are denoted using header or other tags, so it might be easier
    # to figure out when a section starts and ends.
    def getDefinitionsParagraphHTML(self):
        defParagraphLines = [];


        # Go through all the lines before the definitions paragraph.
        for line in self.file:
            if "definition" in line.lower():
                break;



        return defParagraphLines

    def getLines(self):
        lines = []
        for line in self.file:
            lines.append(line)

        return filter(lambda item: item != '\n', lines)
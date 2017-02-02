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

    # Assume paragraph number is the first occurring non-whitespace. If it isn't
    # a number, then there is no paragraph number.
    # Types of numbers that can occur: 1 , 1.0, 1.0., 1. , 1)
    # MIGHT NEED EXPANDING
    def getParagraphNumber(self, string):
        explodedLine = string.split(" ")
        index = 0
        numberString = explodedLine[0]
        # If number contains a trailing bracket eg. 1)
        if ")" in numberString:
            numberString = numberString.replace(")", "")
        # If number contains a trailing semi-colon eg. 1. or 1.0.
        if numberString.endswith('.'):
            numberString = numberString[:-1]

        # The number should not have any trailing characters, so only numbers such as 1.0 or 1 should be left in the number string
        try:
            val = int(float(numberString))
            return val
        except ValueError:
            return False;

    #  Doesn't do anything at the moment, as some text files have no clear sections,
    # so I do not know what comes next after the definitions paragraph to stop.
    # I will make the assumption that sections are numbered, and increment by one, also the section number is always an integer
    def getDefinitionsParagraph(self):
        defParagraphLines = [];

        paragraphNumber = 0
        inDef = False
        # Go through all the lines before the definitions paragraph.
        for line in self.file:
            strippedLine = line.lower().replace(".", "").replace("\n", "");
            # Looks for header containing definitions after lowercased, and stripped of random stuff.
            if "definitions" in strippedLine:
                paragraphNumber = self.getParagraphNumber(line)
                if not paragraphNumber:
                    print line
                    raise ValueError("Definitions paragraph header does not contain a paragraph number!")
                inDef = True
                print paragraphNumber
                print inDef
                break

        for line in self.file:
            if inDef:
                nextParNumber = self.getParagraphNumber(line)
                if nextParNumber == paragraphNumber + 1:
                    inDef = False
                    break
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
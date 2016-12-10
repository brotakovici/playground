class LicenseHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'r')

    def readline(self):
        return self.file.readline()

    def read(self, size):
        return self.file.read(size)

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

    def getLines(self):
        lines = []
        for line in self.file:
            lines.append(line)

        return filter(lambda item: item != '\n', lines)
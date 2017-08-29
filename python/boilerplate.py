from agnostic import io
"""
This is based on utemplate from @pfalcon on github
It allows templating functions to be generated from Jinja2-style string templates on the fly.
In the long-term these can be cached or compiled to bytecode for optimisation
TODO CH, merge changes from utemplate, and undo space insertion/removal logic which was added as workaround
"""

def jinjaToPython(templateResolver, templateJinja):
    # create streams and wire them
    template_in = io.StringIO(templateJinja)
    template_out = io.StringIO()
    c = Compiler(template_in, template_out, loader=templateResolver)
    # do a compile run
    try:
        c.compile()
        return template_out.getvalue()
    except Exception as k:
        raise k

def getTemplateModuleName(templateId):
    return "templates.t_{}".format(templateId)

def saveTemplatePython(templateId, templatePython):
    with open("templates/t_{}.py".format(templateId), "w") as f:
        f.write(templatePython)

def loadTemplateGeneratorFactory(templateId):
    templateModule = __import__(getTemplateModuleName(templateId), globals(), locals(), ["render"] )
    return templateModule.render

def normaliseTemplate(loadedString):
    templateString = ""
    # remove leading, trailing and doubled whitespace, but preserve newlines
    lines = [line for line in loadedString.split("\n") if line is not ""]
    for line in lines:
        templateString += " ".join(line.split()) + "\n"
    return templateString

class Resolver:

    def __init__(self, sourceObj, *a, **k):
        self.sourceObj = sourceObj

    def file_open(self, name):
        assert hasattr(self.sourceObj, name), "Missing {}".format(name)
        loadedString = getattr(self.sourceObj, name)
        assert type(loadedString) == str, "Entry {} not 'str'".format(name)
        normalised = normaliseTemplate(loadedString)
        return io.StringIO(normalised)

class Compiler:

    START_CHAR = "{"
    STMNT = "%"
    STMNT_END = "%}"
    EXPR = "{"
    EXPR_END = "}}"

    def __init__(self, file_in, file_out, indent=0, seq=0, loader=None):
        self.file_in = file_in
        self.file_out = file_out
        self.loader = loader
        self.seq = seq
        self._indent = indent
        self.stack = []
        self.in_literal = False
        self.flushed_header = False
        self.args = "*a, **d"

    def indent(self, adjust=0):
        if not self.flushed_header:
            self.flushed_header = True
            self.indent()
            self.file_out.write("def render%s(%s):\n" % (str(self.seq) if self.seq else "", self.args))
            self.stack.append("def")
        self.file_out.write("    " * (len(self.stack) + self._indent + adjust))

    def literal(self, s):
        if not s:
            return
        if not self.in_literal:
            self.indent()
            self.file_out.write('yield """')
            self.in_literal = True
        self.file_out.write(s.replace('"', '\\"'))

    def close_literal(self):
        if self.in_literal:
            self.file_out.write('"""\n')
        self.in_literal = False

    def render_expr(self, e):
        self.indent()
        self.file_out.write('yield str(' + e + ')\n')

    def parse_statement(self, stmt):
        tokens = stmt.split(None, 1)
        if tokens[0] == "args":
            if len(tokens) > 1:
                self.args = tokens[1]
            else:
                self.args = ""
        elif tokens[0] == "include":
            if not self.flushed_header:
                # If there was no other output, we still need a header now
                self.indent()
            tokens = tokens[1].split(None, 1)
            file_path = tokens[0][1:-1]
            with self.loader.file_open(file_path) as inc:
                self.seq += 1
                c = Compiler(inc, self.file_out, len(self.stack) + self._indent, self.seq, self.loader)
                inc_id = self.seq
                self.seq = c.compile()
            self.indent()
            args = ""
            if len(tokens) > 1:
                args = tokens[1]
            self.file_out.write("yield from render%d(%s)\n" % (inc_id, args))
        elif len(tokens) > 1:
            if tokens[0] == "elif":
                assert self.stack[-1] == "if"
                self.indent(-1)
                self.file_out.write(stmt + ":\n")
            else:
                self.indent()
                self.file_out.write(stmt + ":\n")
                self.stack.append(tokens[0])
        else:
            if stmt.startswith("end"):
                assert self.stack[-1] == stmt[3:]
                self.stack.pop(-1)
            elif stmt == "else":
                assert self.stack[-1] == "if"
                self.indent(-1)
                self.file_out.write("else:\n")
            else:
                assert False

    def parse_line(self, l):
        while l:
            start = l.find(self.START_CHAR)
            if start == -1:
                self.literal(l)
                return
            self.literal(l[:start])
            self.close_literal()
            sel = l[start + 1]
            #print("*%s=%s=" % (sel, EXPR))
            if sel == self.STMNT:
                end = l.find(self.STMNT_END)
                assert end > 0
                stmt = l[start + len(self.START_CHAR + self.STMNT):end].strip()
                self.parse_statement(stmt)
                end += len(self.STMNT_END)
                l = l[end:]
                if not self.in_literal and l == "\n":
                    break
            elif sel == self.EXPR:
                end = l.find(self.EXPR_END)
                assert end > 0
                expr = l[start + len(self.START_CHAR + self.EXPR):end].strip()
                self.render_expr(expr)
                end += len(self.EXPR_END)
                l = l[end:]
            else:
                self.literal(l[start])
                l = l[start + 1:]

    def header(self):
        self.file_out.write("#\n")

    def compile(self):
        self.header()
        for l in self.file_in:
            self.parse_line(l)
        self.close_literal()
        return self.seq
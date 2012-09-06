

class WordProcessor(object):
    PLUGINS = []
    
    @classmethod
    def process(cls, text):
        for plugin in cls.PLUGINS:
            text= plugin().cleanup(text)
        return text

    @classmethod
    def plugin(cls, plgn):
        cls.PLUGINS.append(plgn)



@WordProcessor.plugin
class CleanMDashesExtension(object):
        def cleanup(self, text):
            return text.replace('&mdash;', u'\N{em dash}')


@WordProcessor.plugin
class CleanUpperCase(object):
        def cleanup(self,text):
            return text.lower()


print WordProcessor.process("Hi this is a Test")






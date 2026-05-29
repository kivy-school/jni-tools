from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BreakIterator"]

class BreakIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/BreakIterator"
    DONE = JavaStaticField("I")
    getCharacterInstance = JavaMultipleMethod([("()Ljava/text/BreakIterator;", True, False), ("(Ljava/util/Locale;)Ljava/text/BreakIterator;", True, False)])
    getLineInstance = JavaMultipleMethod([("(Ljava/util/Locale;)Ljava/text/BreakIterator;", True, False), ("()Ljava/text/BreakIterator;", True, False)])
    getSentenceInstance = JavaMultipleMethod([("(Ljava/util/Locale;)Ljava/text/BreakIterator;", True, False), ("()Ljava/text/BreakIterator;", True, False)])
    getWordInstance = JavaMultipleMethod([("()Ljava/text/BreakIterator;", True, False), ("(Ljava/util/Locale;)Ljava/text/BreakIterator;", True, False)])
    isBoundary = JavaMethod("(I)Z")
    preceding = JavaMethod("(I)I")
    following = JavaMethod("(I)I")
    clone = JavaMethod("()Ljava/lang/Object;")
    next = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False)])
    last = JavaMethod("()I")
    first = JavaMethod("()I")
    current = JavaMethod("()I")
    getAvailableLocales = JavaStaticMethod("()[Ljava/util/Locale;")
    getText = JavaMethod("()Ljava/text/CharacterIterator;")
    setText = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/text/CharacterIterator;)V", False, False)])
    previous = JavaMethod("()I")
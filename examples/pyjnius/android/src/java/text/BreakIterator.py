from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BreakIterator"]

class BreakIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/BreakIterator"
    __javaconstructor__ = [("()V", False)]
    DONE = JavaStaticField("I")
    clone = JavaMethod("()Ljava/lang/Object;")
    first = JavaMethod("()I")
    last = JavaMethod("()I")
    next = JavaMultipleMethod([("(I)I", False, False), ("()I", False, False)])
    previous = JavaMethod("()I")
    following = JavaMethod("(I)I")
    preceding = JavaMethod("(I)I")
    isBoundary = JavaMethod("(I)Z")
    current = JavaMethod("()I")
    getText = JavaMethod("()Ljava/text/CharacterIterator;")
    setText = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/text/CharacterIterator;)V", False, False)])
    getWordInstance = JavaMultipleMethod([("()Ljava/text/BreakIterator;", True, False), ("(Ljava/util/Locale;)Ljava/text/BreakIterator;", True, False)])
    getLineInstance = JavaMultipleMethod([("()Ljava/text/BreakIterator;", True, False), ("(Ljava/util/Locale;)Ljava/text/BreakIterator;", True, False)])
    getCharacterInstance = JavaMultipleMethod([("()Ljava/text/BreakIterator;", True, False), ("(Ljava/util/Locale;)Ljava/text/BreakIterator;", True, False)])
    getSentenceInstance = JavaMultipleMethod([("()Ljava/text/BreakIterator;", True, False), ("(Ljava/util/Locale;)Ljava/text/BreakIterator;", True, False)])
    getAvailableLocales = JavaStaticMethod("()[Ljava/util/Locale;")
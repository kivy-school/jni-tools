from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnicodeSetIterator"]

class UnicodeSetIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/UnicodeSetIterator"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/text/UnicodeSet;)V", False)]
    IS_STRING = JavaStaticField("I")
    codepoint = JavaField("I")
    codepointEnd = JavaField("I")
    string = JavaField("Ljava/lang/String;")
    nextRange = JavaMethod("()Z")
    skipToStrings = JavaMethod("()Landroid/icu/text/UnicodeSetIterator;")
    reset = JavaMultipleMethod([("(Landroid/icu/text/UnicodeSet;)V", False, False), ("()V", False, False)])
    next = JavaMethod("()Z")
    getString = JavaMethod("()Ljava/lang/String;")
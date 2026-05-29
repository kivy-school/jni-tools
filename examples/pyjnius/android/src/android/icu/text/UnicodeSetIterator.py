from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnicodeSetIterator"]

class UnicodeSetIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/UnicodeSetIterator"
    __javaconstructor__ = [("(Landroid/icu/text/UnicodeSet;)V", False), ("()V", False)]
    IS_STRING = JavaStaticField("I")
    codepoint = JavaField("I")
    codepointEnd = JavaField("I")
    string = JavaField("Ljava/lang/String;")
    skipToStrings = JavaMethod("()Landroid/icu/text/UnicodeSetIterator;")
    next = JavaMethod("()Z")
    nextRange = JavaMethod("()Z")
    reset = JavaMultipleMethod([("(Landroid/icu/text/UnicodeSet;)V", False, False), ("()V", False, False)])
    getString = JavaMethod("()Ljava/lang/String;")
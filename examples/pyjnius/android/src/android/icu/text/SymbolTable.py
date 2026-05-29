from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SymbolTable"]

class SymbolTable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/SymbolTable"
    SYMBOL_REF = JavaStaticField("C")
    lookupMatcher = JavaMethod("(I)Landroid/icu/text/UnicodeMatcher;")
    parseReference = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;I)Ljava/lang/String;")
    lookup = JavaMethod("(Ljava/lang/String;)[C")
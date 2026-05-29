from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisplayContext"]

class DisplayContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/DisplayContext"
    CAPITALIZATION_FOR_BEGINNING_OF_SENTENCE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    CAPITALIZATION_FOR_MIDDLE_OF_SENTENCE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    CAPITALIZATION_FOR_STANDALONE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    CAPITALIZATION_FOR_UI_LIST_OR_MENU = JavaStaticField("Landroid/icu/text/DisplayContext;")
    CAPITALIZATION_NONE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    DIALECT_NAMES = JavaStaticField("Landroid/icu/text/DisplayContext;")
    LENGTH_FULL = JavaStaticField("Landroid/icu/text/DisplayContext;")
    LENGTH_SHORT = JavaStaticField("Landroid/icu/text/DisplayContext;")
    NO_SUBSTITUTE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    STANDARD_NAMES = JavaStaticField("Landroid/icu/text/DisplayContext;")
    SUBSTITUTE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    type = JavaMethod("()Landroid/icu/text/DisplayContext$Type;")
    value = JavaMethod("()I")
    values = JavaStaticMethod("()[Landroid/icu/text/DisplayContext;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/DisplayContext;")

    class Type(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/DisplayContext$Type"
        CAPITALIZATION = JavaStaticField("Landroid/icu/text/DisplayContext$Type;")
        DIALECT_HANDLING = JavaStaticField("Landroid/icu/text/DisplayContext$Type;")
        DISPLAY_LENGTH = JavaStaticField("Landroid/icu/text/DisplayContext$Type;")
        SUBSTITUTE_HANDLING = JavaStaticField("Landroid/icu/text/DisplayContext$Type;")
        values = JavaStaticMethod("()[Landroid/icu/text/DisplayContext$Type;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/DisplayContext$Type;")
        CAPITALIZATION = JavaStaticField("Landroid/icu/text/DisplayContext$Type;")
        DIALECT_HANDLING = JavaStaticField("Landroid/icu/text/DisplayContext$Type;")
        DISPLAY_LENGTH = JavaStaticField("Landroid/icu/text/DisplayContext$Type;")
        SUBSTITUTE_HANDLING = JavaStaticField("Landroid/icu/text/DisplayContext$Type;")
    CAPITALIZATION_FOR_BEGINNING_OF_SENTENCE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    CAPITALIZATION_FOR_MIDDLE_OF_SENTENCE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    CAPITALIZATION_FOR_STANDALONE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    CAPITALIZATION_FOR_UI_LIST_OR_MENU = JavaStaticField("Landroid/icu/text/DisplayContext;")
    CAPITALIZATION_NONE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    DIALECT_NAMES = JavaStaticField("Landroid/icu/text/DisplayContext;")
    LENGTH_FULL = JavaStaticField("Landroid/icu/text/DisplayContext;")
    LENGTH_SHORT = JavaStaticField("Landroid/icu/text/DisplayContext;")
    NO_SUBSTITUTE = JavaStaticField("Landroid/icu/text/DisplayContext;")
    STANDARD_NAMES = JavaStaticField("Landroid/icu/text/DisplayContext;")
    SUBSTITUTE = JavaStaticField("Landroid/icu/text/DisplayContext;")
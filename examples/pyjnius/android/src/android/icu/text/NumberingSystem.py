from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberingSystem"]

class NumberingSystem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/NumberingSystem"
    __javaconstructor__ = [("()V", False)]
    LATIN = JavaStaticField("Landroid/icu/text/NumberingSystem;")
    getAvailableNames = JavaStaticMethod("()[Ljava/lang/String;")
    getInstanceByName = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/NumberingSystem;")
    getRadix = JavaMethod("()I")
    isAlgorithmic = JavaMethod("()Z")
    isValidDigitString = JavaStaticMethod("(Ljava/lang/String;)Z")
    getName = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/util/Locale;)Landroid/icu/text/NumberingSystem;", True, False), ("()Landroid/icu/text/NumberingSystem;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/text/NumberingSystem;", True, False), ("(IZLjava/lang/String;)Landroid/icu/text/NumberingSystem;", True, False)])
    getDescription = JavaMethod("()Ljava/lang/String;")
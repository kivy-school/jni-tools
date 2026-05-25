from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberingSystem"]

class NumberingSystem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/NumberingSystem"
    __javaconstructor__ = [("()V", False)]
    LATIN = JavaStaticField("Landroid/icu/text/NumberingSystem;")
    getInstance = JavaMultipleMethod([("(IZLjava/lang/String;)Landroid/icu/text/NumberingSystem;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/NumberingSystem;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/text/NumberingSystem;", True, False), ("()Landroid/icu/text/NumberingSystem;", True, False)])
    getInstanceByName = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/NumberingSystem;")
    getAvailableNames = JavaStaticMethod("()[Ljava/lang/String;")
    isValidDigitString = JavaStaticMethod("(Ljava/lang/String;)Z")
    getRadix = JavaMethod("()I")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    isAlgorithmic = JavaMethod("()Z")
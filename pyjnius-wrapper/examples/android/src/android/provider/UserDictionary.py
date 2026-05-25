from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserDictionary"]

class UserDictionary(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/UserDictionary"
    __javaconstructor__ = [("()V", False)]
    AUTHORITY = JavaStaticField("Ljava/lang/String;")
    CONTENT_URI = JavaStaticField("Landroid/net/Uri;")

    class Words(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/UserDictionary/Words"
        __javaconstructor__ = [("()V", False)]
        APP_ID = JavaStaticField("Ljava/lang/String;")
        CONTENT_ITEM_TYPE = JavaStaticField("Ljava/lang/String;")
        CONTENT_TYPE = JavaStaticField("Ljava/lang/String;")
        CONTENT_URI = JavaStaticField("Landroid/net/Uri;")
        DEFAULT_SORT_ORDER = JavaStaticField("Ljava/lang/String;")
        FREQUENCY = JavaStaticField("Ljava/lang/String;")
        LOCALE = JavaStaticField("Ljava/lang/String;")
        LOCALE_TYPE_ALL = JavaStaticField("I")
        LOCALE_TYPE_CURRENT = JavaStaticField("I")
        SHORTCUT = JavaStaticField("Ljava/lang/String;")
        WORD = JavaStaticField("Ljava/lang/String;")
        _ID = JavaStaticField("Ljava/lang/String;")
        addWord = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/String;II)V", True, False), ("(Landroid/content/Context;Ljava/lang/String;ILjava/lang/String;Ljava/util/Locale;)V", True, False)])
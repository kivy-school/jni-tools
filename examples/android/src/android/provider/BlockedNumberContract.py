from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlockedNumberContract"]

class BlockedNumberContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/BlockedNumberContract"
    AUTHORITY = JavaStaticField("Ljava/lang/String;")
    AUTHORITY_URI = JavaStaticField("Landroid/net/Uri;")
    isBlocked = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Z")
    unblock = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)I")
    canCurrentUserBlockNumbers = JavaStaticMethod("(Landroid/content/Context;)Z")

    class BlockedNumbers(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/BlockedNumberContract/BlockedNumbers"
        COLUMN_E164_NUMBER = JavaStaticField("Ljava/lang/String;")
        COLUMN_ID = JavaStaticField("Ljava/lang/String;")
        COLUMN_ORIGINAL_NUMBER = JavaStaticField("Ljava/lang/String;")
        CONTENT_ITEM_TYPE = JavaStaticField("Ljava/lang/String;")
        CONTENT_TYPE = JavaStaticField("Ljava/lang/String;")
        CONTENT_URI = JavaStaticField("Landroid/net/Uri;")
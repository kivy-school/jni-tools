from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisplayHashResultCallback"]

class DisplayHashResultCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/displayhash/DisplayHashResultCallback"
    DISPLAY_HASH_ERROR_INVALID_BOUNDS = JavaStaticField("I")
    DISPLAY_HASH_ERROR_INVALID_HASH_ALGORITHM = JavaStaticField("I")
    DISPLAY_HASH_ERROR_MISSING_WINDOW = JavaStaticField("I")
    DISPLAY_HASH_ERROR_NOT_VISIBLE_ON_SCREEN = JavaStaticField("I")
    DISPLAY_HASH_ERROR_TOO_MANY_REQUESTS = JavaStaticField("I")
    DISPLAY_HASH_ERROR_UNKNOWN = JavaStaticField("I")
    onDisplayHashError = JavaMethod("(I)V")
    onDisplayHashResult = JavaMethod("(Landroid/view/displayhash/DisplayHash;)V")
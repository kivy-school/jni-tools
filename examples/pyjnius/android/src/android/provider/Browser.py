from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Browser"]

class Browser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/Browser"
    __javaconstructor__ = [("()V", False)]
    EXTRA_APPLICATION_ID = JavaStaticField("Ljava/lang/String;")
    EXTRA_CREATE_NEW_TAB = JavaStaticField("Ljava/lang/String;")
    EXTRA_HEADERS = JavaStaticField("Ljava/lang/String;")
    INITIAL_ZOOM_LEVEL = JavaStaticField("Ljava/lang/String;")
    sendString = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)V")
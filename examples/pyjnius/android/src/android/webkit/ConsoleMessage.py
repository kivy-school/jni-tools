from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConsoleMessage"]

class ConsoleMessage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/ConsoleMessage"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;ILandroid/webkit/ConsoleMessage$MessageLevel;)V", False)]
    lineNumber = JavaMethod("()I")
    message = JavaMethod("()Ljava/lang/String;")
    sourceId = JavaMethod("()Ljava/lang/String;")
    messageLevel = JavaMethod("()Landroid/webkit/ConsoleMessage$MessageLevel;")

    class MessageLevel(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/ConsoleMessage$MessageLevel"
        DEBUG = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
        ERROR = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
        LOG = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
        TIP = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
        WARNING = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
        values = JavaStaticMethod("()[Landroid/webkit/ConsoleMessage$MessageLevel;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/webkit/ConsoleMessage$MessageLevel;")
        DEBUG = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
        ERROR = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
        LOG = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
        TIP = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
        WARNING = JavaStaticField("Landroid/webkit/ConsoleMessage$MessageLevel;")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessageContentKt"]

class OSInAppMessageContentKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessageContentKt"
    HTML = JavaStaticField("Ljava/lang/String;")
    STYLES = JavaStaticField("Ljava/lang/String;")
    DISPLAY_DURATION = JavaStaticField("Ljava/lang/String;")
    REMOVE_HEIGHT_MARGIN = JavaStaticField("Ljava/lang/String;")
    REMOVE_WIDTH_MARGIN = JavaStaticField("Ljava/lang/String;")
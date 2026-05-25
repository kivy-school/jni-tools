from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimedText"]

class TimedText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/TimedText"
    getText = JavaMethod("()Ljava/lang/String;")
    getBounds = JavaMethod("()Landroid/graphics/Rect;")
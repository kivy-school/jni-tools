from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimedText"]

class TimedText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/TimedText"
    getBounds = JavaMethod("()Landroid/graphics/Rect;")
    getText = JavaMethod("()Ljava/lang/String;")
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PostProcessor"]

class PostProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PostProcessor"
    onPostProcess = JavaMethod("(Landroid/graphics/Canvas;)I")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PostProcessor"]

class PostProcessor(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PostProcessor"
    onPostProcess = JavaMethod("(Landroid/graphics/Canvas;)I")
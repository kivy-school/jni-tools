from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Movie"]

class Movie(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Movie"
    width = JavaMethod("()I")
    height = JavaMethod("()I")
    isOpaque = JavaMethod("()Z")
    duration = JavaMethod("()I")
    setTime = JavaMethod("(I)Z")
    draw = JavaMultipleMethod([("(Landroid/graphics/Canvas;FFLandroid/graphics/Paint;)V", False, False), ("(Landroid/graphics/Canvas;FF)V", False, False)])
    decodeStream = JavaStaticMethod("(Ljava/io/InputStream;)Landroid/graphics/Movie;")
    decodeByteArray = JavaStaticMethod("([BII)Landroid/graphics/Movie;")
    decodeFile = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/Movie;")
    finalize = JavaMethod("()V")
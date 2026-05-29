from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Movie"]

class Movie(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Movie"
    decodeStream = JavaStaticMethod("(Ljava/io/InputStream;)Landroid/graphics/Movie;")
    decodeFile = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/Movie;")
    decodeByteArray = JavaStaticMethod("([BII)Landroid/graphics/Movie;")
    duration = JavaMethod("()I")
    isOpaque = JavaMethod("()Z")
    draw = JavaMultipleMethod([("(Landroid/graphics/Canvas;FFLandroid/graphics/Paint;)V", False, False), ("(Landroid/graphics/Canvas;FF)V", False, False)])
    width = JavaMethod("()I")
    height = JavaMethod("()I")
    setTime = JavaMethod("(I)Z")
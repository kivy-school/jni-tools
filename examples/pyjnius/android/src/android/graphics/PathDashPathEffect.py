from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathDashPathEffect"]

class PathDashPathEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PathDashPathEffect"
    __javaconstructor__ = [("(Landroid/graphics/Path;FFLandroid/graphics/PathDashPathEffect$Style;)V", False)]

    class Style(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/PathDashPathEffect$Style"
        MORPH = JavaStaticField("Landroid/graphics/PathDashPathEffect$Style;")
        ROTATE = JavaStaticField("Landroid/graphics/PathDashPathEffect$Style;")
        TRANSLATE = JavaStaticField("Landroid/graphics/PathDashPathEffect$Style;")
        values = JavaStaticMethod("()[Landroid/graphics/PathDashPathEffect$Style;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/PathDashPathEffect$Style;")
        MORPH = JavaStaticField("Landroid/graphics/PathDashPathEffect$Style;")
        ROTATE = JavaStaticField("Landroid/graphics/PathDashPathEffect$Style;")
        TRANSLATE = JavaStaticField("Landroid/graphics/PathDashPathEffect$Style;")
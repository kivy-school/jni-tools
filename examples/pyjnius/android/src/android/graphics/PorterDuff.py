from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PorterDuff"]

class PorterDuff(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PorterDuff"
    __javaconstructor__ = [("()V", False)]

    class Mode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/PorterDuff$Mode"
        ADD = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        CLEAR = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DARKEN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST_ATOP = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST_IN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST_OUT = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST_OVER = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        LIGHTEN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        MULTIPLY = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        OVERLAY = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SCREEN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC_ATOP = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC_IN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC_OUT = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC_OVER = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        XOR = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        values = JavaStaticMethod("()[Landroid/graphics/PorterDuff$Mode;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/PorterDuff$Mode;")
        ADD = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        CLEAR = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DARKEN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST_ATOP = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST_IN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST_OUT = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        DST_OVER = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        LIGHTEN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        MULTIPLY = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        OVERLAY = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SCREEN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC_ATOP = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC_IN = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC_OUT = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        SRC_OVER = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
        XOR = JavaStaticField("Landroid/graphics/PorterDuff$Mode;")
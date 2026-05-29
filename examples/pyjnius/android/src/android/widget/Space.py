from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Space"]

class Space(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Space"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    onMeasure = JavaMethod("(II)V")
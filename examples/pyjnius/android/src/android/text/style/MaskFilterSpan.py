from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MaskFilterSpan"]

class MaskFilterSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/MaskFilterSpan"
    __javaconstructor__ = [("(Landroid/graphics/MaskFilter;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    getMaskFilter = JavaMethod("()Landroid/graphics/MaskFilter;")
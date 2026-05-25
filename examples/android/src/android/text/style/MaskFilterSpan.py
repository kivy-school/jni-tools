from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MaskFilterSpan"]

class MaskFilterSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/MaskFilterSpan"
    __javaconstructor__ = [("(Landroid/graphics/MaskFilter;)V", False)]
    getMaskFilter = JavaMethod("()Landroid/graphics/MaskFilter;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")
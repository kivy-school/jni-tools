from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextPaint"]

class TextPaint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/TextPaint"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Landroid/graphics/Paint;)V", False)]
    baselineShift = JavaField("I")
    bgColor = JavaField("I")
    density = JavaField("F")
    drawableState = JavaField("[I")
    linkColor = JavaField("I")
    underlineColor = JavaField("I")
    underlineThickness = JavaField("F")
    set = JavaMethod("(Landroid/text/TextPaint;)V")
    getUnderlineThickness = JavaMethod("()F")
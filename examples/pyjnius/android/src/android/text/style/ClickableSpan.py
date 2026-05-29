from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClickableSpan"]

class ClickableSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/ClickableSpan"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    onClick = JavaMethod("(Landroid/view/View;)V")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
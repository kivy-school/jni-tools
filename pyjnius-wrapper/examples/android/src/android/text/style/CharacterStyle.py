from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharacterStyle"]

class CharacterStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/CharacterStyle"
    __javaconstructor__ = [("()V", False)]
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    wrap = JavaStaticMethod("(Landroid/text/style/CharacterStyle;)Landroid/text/style/CharacterStyle;")
    getUnderlying = JavaMethod("()Landroid/text/style/CharacterStyle;")
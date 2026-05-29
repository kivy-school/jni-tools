from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharacterStyle"]

class CharacterStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/CharacterStyle"
    __javaconstructor__ = [("()V", False)]
    wrap = JavaStaticMethod("(Landroid/text/style/CharacterStyle;)Landroid/text/style/CharacterStyle;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    getUnderlying = JavaMethod("()Landroid/text/style/CharacterStyle;")
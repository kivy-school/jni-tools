from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FontFamily"]

class FontFamily(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/FontFamily"
    getFont = JavaMethod("(I)Landroid/graphics/fonts/Font;")
    getSize = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/fonts/FontFamily/Builder"
        __javaconstructor__ = [("(Landroid/graphics/fonts/Font;)V", False)]
        addFont = JavaMethod("(Landroid/graphics/fonts/Font;)Landroid/graphics/fonts/FontFamily$Builder;")
        buildVariableFamily = JavaMethod("()Landroid/graphics/fonts/FontFamily;")
        build = JavaMethod("()Landroid/graphics/fonts/FontFamily;")
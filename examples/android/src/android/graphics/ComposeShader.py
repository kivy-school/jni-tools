from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComposeShader"]

class ComposeShader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ComposeShader"
    __javaconstructor__ = [("(Landroid/graphics/Shader;Landroid/graphics/Shader;Landroid/graphics/Xfermode;)V", False), ("(Landroid/graphics/Shader;Landroid/graphics/Shader;Landroid/graphics/PorterDuff$Mode;)V", False), ("(Landroid/graphics/Shader;Landroid/graphics/Shader;Landroid/graphics/BlendMode;)V", False)]
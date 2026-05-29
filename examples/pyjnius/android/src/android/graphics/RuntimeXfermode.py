from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RuntimeXfermode"]

class RuntimeXfermode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/RuntimeXfermode"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    setFloatUniform = JavaMultipleMethod([("(Ljava/lang/String;F)V", False, False), ("(Ljava/lang/String;FF)V", False, False), ("(Ljava/lang/String;FFF)V", False, False), ("(Ljava/lang/String;FFFF)V", False, False), ("(Ljava/lang/String;[F)V", False, False)])
    setIntUniform = JavaMultipleMethod([("(Ljava/lang/String;I)V", False, False), ("(Ljava/lang/String;IIII)V", False, False), ("(Ljava/lang/String;III)V", False, False), ("(Ljava/lang/String;II)V", False, False), ("(Ljava/lang/String;[I)V", False, False)])
    setColorUniform = JavaMultipleMethod([("(Ljava/lang/String;J)V", False, False), ("(Ljava/lang/String;Landroid/graphics/Color;)V", False, False), ("(Ljava/lang/String;I)V", False, False)])
    setInputXfermode = JavaMethod("(Ljava/lang/String;Landroid/graphics/RuntimeXfermode;)V")
    setInputShader = JavaMethod("(Ljava/lang/String;Landroid/graphics/Shader;)V")
    setInputColorFilter = JavaMethod("(Ljava/lang/String;Landroid/graphics/ColorFilter;)V")
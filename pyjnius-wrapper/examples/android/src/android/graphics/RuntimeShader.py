from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RuntimeShader"]

class RuntimeShader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/RuntimeShader"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    setColorUniform = JavaMultipleMethod([("(Ljava/lang/String;I)V", False, False), ("(Ljava/lang/String;J)V", False, False), ("(Ljava/lang/String;Landroid/graphics/Color;)V", False, False)])
    setFloatUniform = JavaMultipleMethod([("(Ljava/lang/String;F)V", False, False), ("(Ljava/lang/String;FF)V", False, False), ("(Ljava/lang/String;FFF)V", False, False), ("(Ljava/lang/String;FFFF)V", False, False), ("(Ljava/lang/String;[F)V", False, False)])
    setIntUniform = JavaMultipleMethod([("(Ljava/lang/String;I)V", False, False), ("(Ljava/lang/String;II)V", False, False), ("(Ljava/lang/String;III)V", False, False), ("(Ljava/lang/String;IIII)V", False, False), ("(Ljava/lang/String;[I)V", False, False)])
    setInputShader = JavaMethod("(Ljava/lang/String;Landroid/graphics/Shader;)V")
    setInputBuffer = JavaMethod("(Ljava/lang/String;Landroid/graphics/BitmapShader;)V")
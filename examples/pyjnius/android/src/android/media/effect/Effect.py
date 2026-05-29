from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Effect"]

class Effect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/effect/Effect"
    __javaconstructor__ = [("()V", False)]
    setUpdateListener = JavaMethod("(Landroid/media/effect/EffectUpdateListener;)V")
    setParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getName = JavaMethod("()Ljava/lang/String;")
    apply = JavaMethod("(IIII)V")
    release = JavaMethod("()V")
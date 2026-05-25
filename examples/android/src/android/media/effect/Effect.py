from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Effect"]

class Effect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/effect/Effect"
    __javaconstructor__ = [("()V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    apply = JavaMethod("(IIII)V")
    setParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    setUpdateListener = JavaMethod("(Landroid/media/effect/EffectUpdateListener;)V")
    release = JavaMethod("()V")
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EffectContext"]

class EffectContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/effect/EffectContext"
    createWithCurrentGlContext = JavaStaticMethod("()Landroid/media/effect/EffectContext;")
    getFactory = JavaMethod("()Landroid/media/effect/EffectFactory;")
    release = JavaMethod("()V")